from django.urls import path
from .views import Api, NoApi

urlpatterns = [
    path('api/', NoApi.as_view()),
    path('api/<id>', Api.as_view()),
]
