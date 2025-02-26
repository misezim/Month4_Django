from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

junior_dev = 'Заработная плата Младшего разработчика составляет 600$'
middle_dev = 'Заработная плата Продолжающего разработчика составляет 900$'
senior_dev= 'Заработная плата Старшего разработчика составляет 1500$'
team_lead_dev = 'Заработная плата Тим Лида составляет 2000$'

class SalaryExperienceMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            experience = int(request.POST.get('experience'))
            if experience<1:
                return HttpResponseBadRequest('У вас должен быть опыт минимум 1 год')
            elif experience>=1 and experience<3:
                request.salary = junior_dev
            elif experience>=3 and experience<4:
                request.salary = middle_dev
            elif experience>=4 and experience<5:
                request.salary = senior_dev
            elif experience>=5 and experience<=7:
                request.salary = team_lead_dev
            else:
                return HttpResponseBadRequest('Мы не сможем соответствовать вашим ожиданиям по заработной плате')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'salary', 'Ставка не определена')