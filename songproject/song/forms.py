from django import forms
from .models import Song


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"

        widgets = {
            "song_name": forms.TextInput(attrs={'class': 'form-control'}),
            "lyricist": forms.TextInput(attrs={'class': 'form-control'}),
            "music_composer": forms.TextInput(attrs={'class': 'form-control'}),
            "from_movie": forms.TextInput(attrs={'class': 'form-control'}),
            "label": forms.Select(attrs={'class': 'form-control'}),
        }
