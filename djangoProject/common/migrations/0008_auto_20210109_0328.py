# Generated by Django 3.1.5 on 2021-01-09 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20210109_0248'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='ordermedicine',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='ordermedicine',
            name='order',
        ),
        migrations.RemoveField(
            model_name='student',
            name='country',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.DeleteModel(
            name='OrderMedicine',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
