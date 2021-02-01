from django.urls import path

from music import views

urlpatterns = [
    path('index',views.music_view),
]