from django.urls import path
from . import views

app_name = 'music_player'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_song, name='upload'),
    path('profile/', views.profile_view, name='profile'),
    path('delete/<int:song_id>/', views.delete_song, name='delete'),
    path('settings/', views.settings_view, name='settings'),
]