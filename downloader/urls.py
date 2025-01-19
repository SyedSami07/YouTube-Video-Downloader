from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.download_video, name='download_video'),
    path('about/',views.about, name='about'),
]
