# Generated by Django 3.1.4 on 2021-01-01 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_customer_qq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='qq',
        ),
    ]
