from django.shortcuts import render
from .models import *


def common_data():
    return {
        "posts": Post.objects.all(),
        "header": GeneralHeader.objects.get(page_name='0'),
        "nav": Navbar.objects.all(),
        "txt": FooterText.objects.last(),
        "foot": Footer.objects.all()
    }


def index_view(request):
    context = common_data()
    return render(request, 'home_page/index.html', context)


def base_view(request):
    context = common_data()
    context["user"] = get_user_model()
    return render(request, 'base/base.html', context)


def about_view(request):
    context = common_data()
    context["header"] = GeneralHeader.objects.get(page_name=1)
    return render(request, 'about_page/about.html', context)
