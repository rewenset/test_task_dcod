from django.conf.urls import url
from . import views

app_name = 'chart'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]