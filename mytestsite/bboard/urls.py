# Используем базовую библиотеку
from django.urls import path

# Импортируем контролллер из views.py
from .views import index

# Добавляем пути для контроллеров приложения
urlpatterns = [
    path('', index),
]