from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Song
from .forms import SongForm
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

def index(request):
    songs = Song.objects.all().order_by('-uploaded_at')
    return render(request, 'music_player/index.html', {'songs': songs})

@login_required
def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.uploaded_by = request.user
            song.save()
            messages.success(request, 'Song uploaded successfully!')
            return redirect('index')
    else:
        form = SongForm()
    return render(request, 'music_player/upload.html', {'form': form})

@login_required
def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.user == song.uploaded_by or request.user.is_superuser:
        song.delete()
        messages.success(request, 'Song deleted successfully!')
    else:
        messages.error(request, 'You are not authorized to delete this song.')
    return redirect('index')

@login_required
def profile_view(request):
    return render(request, 'music_player/profile.html')
@login_required
def settings_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                  request.FILES, 
                                  instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('music_player:settings')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'music_player/settings.html', context)