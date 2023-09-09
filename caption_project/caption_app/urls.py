from django.urls import path
from . import views

urlpatterns = [
    path('', views.caption_generator, name='caption_generator'),
]