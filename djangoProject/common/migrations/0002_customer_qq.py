# Generated by Django 3.1.4 on 2020-12-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='qq',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
