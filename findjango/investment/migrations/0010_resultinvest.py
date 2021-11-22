# Generated by Django 3.2.9 on 2021-11-22 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investment', '0009_auto_20211119_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultInvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_value', models.DecimalField(decimal_places=7, max_digits=14)),
                ('result_value', models.DecimalField(decimal_places=7, max_digits=14)),
                ('invest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='investment.createinvest')),
                ('investor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='investor_result', to=settings.AUTH_USER_MODEL)),
                ('member', models.ManyToManyField(blank=True, related_name='member_result', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]