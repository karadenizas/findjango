# Generated by Django 3.2.9 on 2021-11-18 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_auto_20211118_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenttransaction',
            name='transaction_type',
            field=models.CharField(choices=[('buy', 'Buying Transactions'), ('sell', 'Selling Transactions')], max_length=10),
        ),
    ]
