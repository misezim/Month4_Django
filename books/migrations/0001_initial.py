# Generated by Django 5.1.5 on 2025-02-08 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='films/', verbose_name='загрузите фото')),
                ('title', models.CharField(max_length=100, verbose_name='укажите название книги')),
                ('description', models.TextField(blank=True, verbose_name='укажите описание книги')),
                ('price', models.PositiveIntegerField(default=200, verbose_name='укажите цену')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('Science Fiction ', 'Science Fiction '), ('Thriller', 'Thriller'), ('Fantasy', 'Fantasy'), ('Biography', 'Biography'), ('Poetry', 'Poetry'), ('Science', 'Science'), ('Philosophy', 'Philosophy')], default='Fantasy', max_length=100, verbose_name='выберите жанр')),
                ('email_address', models.TextField(verbose_name='укажите почту автора')),
                ('director', models.CharField(default='Лев Толстой', max_length=100)),
                ('trailer', models.URLField(verbose_name='укажите ссылку из YOUTUBE')),
            ],
        ),
    ]
