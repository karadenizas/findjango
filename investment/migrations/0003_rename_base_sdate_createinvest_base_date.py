# Generated by Django 3.2.9 on 2021-11-13 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0002_rename_base_date_createinvest_base_sdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createinvest',
            old_name='base_sdate',
            new_name='base_date',
        ),
    ]
