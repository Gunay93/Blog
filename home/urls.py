from .views import *
from django.conf.urls import url

app_name = 'home'
urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^about$', about_view, name='about'),
]
