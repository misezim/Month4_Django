# Generated by Django 5.1.5 on 2025-02-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'verbose_name': 'книга', 'verbose_name_plural': 'книги'},
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='email_address',
            field=models.CharField(max_length=100, verbose_name='укажите почту автора'),
        ),
    ]
