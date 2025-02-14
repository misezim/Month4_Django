from django.db import models
from books.models import BookModel

class BasketModel(models.Model):
    CHOICES = (
        ("В обработке", "В обработке"),
        ("Отправлен", "Отправлен"),
        ("Доставлен", "Доставлен"),
        ("Отменен", "Отменен")
    )
    choice_book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    choice_status = models.CharField(max_length=100, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100)
    order_comments = models.TextField(default="Оставьте под дверью")

    def __str__(self):
        return self.choice_status
