from django.shortcuts import render
from django.http import HttpResponse
from . import models


def all_clothes(request):
    if request.method == 'GET':
        query = models.Clothes.objects.all().order_by('-id')
        context_object_name = {
            'all_clothes': query,
        }
        return render(request, template_name='clothes/all_clothes.html',
                      context=context_object_name)

def kids_clothes(request):
    if request.method == 'GET':
        query = models.Clothes.objects.filter(tags__name = 'детская').order_by('-id')
        context_object_name = {
            'kids_clothes': query,
        }
        return render(request, template_name='clothes/kids.html',
                      context=context_object_name)

def teens_clothes(request):
    if request.method == 'GET':
        query = models.Clothes.objects.filter(tags__name = 'подростковая').order_by('-id')
        context_object_name = {
            'teens_clothes': query,
        }
        return render(request, template_name='clothes/teens.html',
                      context=context_object_name)

def adults_clothes(request):
    if request.method == 'GET':
        query = models.Clothes.objects.filter(tags__name = 'взрослая').order_by('-id')
        context_object_name = {
            'adults_clothes': query,
        }
        return render(request, template_name='clothes/adults.html',
                      context=context_object_name)