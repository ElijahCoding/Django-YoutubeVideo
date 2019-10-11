from .models import Video
from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
        labels = {'url': 'YouTube Url'}