from django import forms
from .models import Song
from django.contrib.auth.models import User
from .models import Profile

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'album', 'audio_file', 'cover_image']
        widgets = {
            'audio_file': forms.FileInput(attrs={'accept': 'audio/*'}),
            'cover_image': forms.FileInput(attrs={'accept': 'image/*'}),
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
