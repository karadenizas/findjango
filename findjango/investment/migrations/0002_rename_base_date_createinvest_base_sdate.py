# Generated by Django 3.2.9 on 2021-11-13 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createinvest',
            old_name='base_date',
            new_name='base_sdate',
        ),
    ]
