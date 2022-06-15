from django.shortcuts import render
from .models import Upload


# Create your views here.


def index(request):

    data = {

        'title': 'Главная страница',

    }

    return render(request, 'main/index.html', data)


def files(request):

    content = Upload.objects.order_by('-date')[:3]
    return render(request, "main/files.html", {'content':content})


