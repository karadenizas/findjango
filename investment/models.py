from datetime import date, datetime
from django.db import models
from userprofile.models import MyUser
from django.utils.timezone import now
from datetime import date
from django.core.exceptions import ValidationError
from django.urls import reverse
import decimal


class CreateInvest(models.Model): #CreateInvest name will change! like InvestAdvice or Invest
    investor = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='investments')
    target_value = models.DecimalField(max_digits=14, decimal_places=7)
    base_currency = models.CharField(max_length=3)
    target_currency = models.CharField(max_length=3)
    create_time = models.DateTimeField(auto_now_add=True)
    base_date = models.DateField(auto_now_add=True)
    target_date = models.DateField(default=now)
    description = models.TextField(max_length=500, null=True)
    analysis = models.TextField(max_length=3000, default='')
    member = models.ManyToManyField(MyUser, blank=True, related_name='invest')
    token = models.IntegerField(null=True, default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-create_time']

    def __str__(self):
        return f'{self.base_currency} to {self.target_currency} by {self.investor}'

    # def save(self, *args, **kwargs):
    #     today = date.today()
    #     if self.target_date <= today:
    #         raise ValidationError('Target date cannot be previous date and today.')
    #     super(CreateInvest, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('investment:detail_invest', kwargs={'id': self.id})


# This model may not be best choice. It will be researched.
class ResultInvest(models.Model):
    invest = models.OneToOneField(CreateInvest, on_delete=models.CASCADE, related_name='result')
    investor = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='investor_result')
    member = models.ManyToManyField(MyUser, blank=True, related_name='member_result')
    create_date = models.DateField(auto_now_add=True)
    start_value = models.DecimalField(max_digits=14, decimal_places=7)
    result_value = models.DecimalField(max_digits=14, decimal_places=7)
    total_value = models.DecimalField(max_digits=14, decimal_places=7, default=0)
    ratio = models.DecimalField(max_digits=14, decimal_places=7, default=0)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return f'{self.start_value} to {self.result_value}'

    def save(self, *args, **kwargs):
        self.total_value = self.start_value - decimal.Decimal(self.result_value)
        self.ratio = ((self.start_value - decimal.Decimal(self.result_value)) / self.start_value) * 100
        return super().save(*args, **kwargs)