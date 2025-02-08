from django.db import models

class BookModel(models.Model):
    GENRE_CHOICES = (
        ('Science Fiction ', 'Science Fiction '),
        ('Thriller', 'Thriller'),
        ('Fantasy', 'Fantasy'),
        ('Biography', 'Biography'),
        ('Poetry', 'Poetry'),
        ('Science', 'Science'),
        ('Philosophy', 'Philosophy'),
    )
    image = models.ImageField(upload_to='films/', verbose_name='загрузите фото')
    title = models.CharField(max_length=100, verbose_name='укажите название книги')
    description = models.TextField(verbose_name='укажите описание книги', blank=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену', default=200)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, default='Fantasy',
                             verbose_name='выберите жанр')
    email_address = models.CharField(max_length=100, verbose_name='укажите почту автора')
    director = models.CharField(max_length=100, default='Лев Толстой')
    trailer = models.URLField(verbose_name='укажите ссылку из YOUTUBE')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'