from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Slider
from marmeladmira.settings import MEDIA_URL, BASE_DIR


# Create your views here.


def index(request):
    return render(request, '/home/khamzat/PycharmProjects/marmelad/marmeladmira/market/templates/market/index.html',)
