# Generated by Django 4.0.4 on 2022-11-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_ordermodel_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_served',
            field=models.BooleanField(default=False),
        ),
    ]