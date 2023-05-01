from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from market.models import *


# Create your views here.


def index(request):
    sliders = SliderImage.objects.all()
    return render(request, '/home/khamzat/PycharmProjects/marmelad/marmeladmira/market/templates/market/index.html',
                  {'sliders': sliders})
