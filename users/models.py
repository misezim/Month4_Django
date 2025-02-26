from django.db import models
from django.contrib.auth.models import User

junior_dev = 'Заработная плата Младшего разработчика составляет 600$'
middle_dev = 'Заработная плата Продолжающего разработчика составляет 900$'
senior_dev= 'Заработная плата Старшего разработчика составляет 1500$'
team_lead_dev = 'Заработная плата Тим Лида составляет 2000$'

class CustomUser(User):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_number = models.CharField(max_length=14, default='+996')
    #важное для для middlewares для проверки возраста
    experience = models.PositiveIntegerField(default=2)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default= 'M')
    salary = models.CharField(max_length=255, default=junior_dev)

    education = models.CharField(max_length=250, blank=False, null=False)
    last_job = models.CharField(max_length=250, blank=True, null=True)
    projects = models.TextField(max_length=250,blank=True, null=True)
    programming_languages = models.TextField(max_length=250,blank=False, null=False)
    awards = models.TextField(max_length=250,blank=True, null=True)
    address = models.TextField(max_length=250,blank=False, null=False)

    def save(self, *args, **kwargs):
        if self.experience<1:
            self.salary = 'У вас должен быть опыт минимум 1 год'
        elif 1<= self.experience <3:
            self.salary = junior_dev
        elif 3<= self.experience <4:
            self.salary = middle_dev
        elif 4<= self.experience <5:
            self.salary = senior_dev
        elif 5<= self.experience <=7:
            self.salary = team_lead_dev
        else:
            self.salary = 'Мы не сможем соответствовать вашим ожиданиям по заработной плате'
        super().save(*args, **kwargs)