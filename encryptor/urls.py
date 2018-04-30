from django.urls import path

from . import views

app_name = 'encryptor'

urlpatterns = [
	path('', views.index, name='index'),
	path('decrypt/', views.decrypt, name='decrypt'),
]