from django import forms
from . import models, parser_mybook, parser_rezka

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('book.yandex.ru', 'book.yandex.ru'),
        ('rezka.ag', 'rezka.ag'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'book.yandex.ru':
            mybook_book = parser_mybook.parsing_mybook()
            for i in mybook_book:
                models.MybookModel.objects.create(**i)
        elif self.data['media_type'] == 'rezka.ag':
            rezka_films = parser_rezka.parsing_rezka()
            for i in rezka_films:
                models.RezkaModel.objects.create(**i)