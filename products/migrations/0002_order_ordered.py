# Generated by Django 3.0.11 on 2020-11-27 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False, verbose_name='Заказано'),
        ),
    ]
