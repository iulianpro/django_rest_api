from django.urls import path
from .views import GetApi, PostApi

urlpatterns = [
    path('api/', PostApi.as_view()),
    path('api/<id>', GetApi.as_view()),
]
