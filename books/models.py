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

class Review(models.Model):
    STARS = (
        ("🌟", "🌟"),
        ("🌟🌟", "🌟🌟"),
        ("🌟🌟🌟", "🌟🌟🌟"),
        ("🌟🌟🌟🌟", "🌟🌟🌟🌟"),
        ("🌟🌟🌟🌟🌟", "🌟🌟🌟🌟🌟"),
    )
    choice_show = models.ForeignKey(BookModel, on_delete=models.CASCADE,
                                    related_name='books')
    created_at = models.DateField(auto_now_add=True)
    review_text = models.TextField(default='Интересная книга! Рекомендую!')
    stars = models.CharField(max_length=10, choices=STARS, default='🌟🌟🌟🌟🌟')
    def __str__(self):
        return f'{self.stars}-{self.choice_show.title}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

# class Comment(models.Model):
#     choice_book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='comments')
#     comment_text = models.TextField(verbose_name='Оставьте комментарий')
#     created_at = models.DateField(auto_now_add=True)
#     def __str__(self):
#         return self.comment_text
