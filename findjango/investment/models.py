from datetime import date, datetime
from django.db import models
from userprofile.models import MyUser
from django.utils.timezone import now
from datetime import date
from django.core.exceptions import ValidationError


class CreateInvest(models.Model): #CreateInvest name will change! like InvestAdvice or Invest
    investor = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='investments')
    target_value = models.DecimalField(max_digits=14, decimal_places=7)
    base_currency = models.CharField(max_length=3)
    target_currency = models.CharField(max_length=3)
    create_time = models.DateTimeField(auto_now_add=True)
    base_date = models.DateField(auto_now_add=True)
    target_date = models.DateField(default=now)

    def __str__(self):
        return f'{self.base_currency} to {self.target_currency} by {self.investor}'

    def save(self, *args, **kwargs):
        today = date.today()
        if self.target_date <= today:
            raise ValidationError('Target date cannot be previous date and now.')
        super(CreateInvest, self).save(*args, **kwargs)