# Generated by Django 3.2.9 on 2021-11-16 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0007_alter_createinvest_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='createinvest',
            name='token',
            field=models.IntegerField(default=0, null=True),
        ),
    ]