from django.contrib import admin
from .models import Song, Profile

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album', 'uploaded_by', 'uploaded_at')
    search_fields = ('title', 'artist', 'album')
    list_filter = ('uploaded_at',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')
