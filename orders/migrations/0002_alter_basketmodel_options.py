# Generated by Django 5.1.5 on 2025-02-21 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basketmodel',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
