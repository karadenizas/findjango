# Generated by Django 3.2.9 on 2021-11-22 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investment', '0010_resultinvest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultinvest',
            name='investor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investor_result', to=settings.AUTH_USER_MODEL),
        ),
    ]
