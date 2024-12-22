from django.http import HttpResponse
from django.shortcuts import render

from .models import CustomUser


def get_proxi_m(request):
    user = CustomUser.objects.all()
    for i in user:
        print(i.get_last_name())
        print(i.ageuser.age)
    return HttpResponse("Oki")