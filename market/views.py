from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Slider
from marmeladmira.settings import MEDIA_URL, BASE_DIR


# Create your views here.


def index(request):
    images = Slider.objects.all()
    context = {'images': images,
               'media': MEDIA_URL,
               'dir': BASE_DIR}

    return render(request, '/home/khamzat/PycharmProjects/marmelad/marmeladmira/market/templates/market/index.html',
                  context=context)
