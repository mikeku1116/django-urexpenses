from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('update/<str:pk>', views.update, name='Update')
]
