from django.forms import ModelForm
from .models import Comentarios
from django import forms


class CommentForm(ModelForm):
    class Meta: 
        model = Comentarios
        fields = ('texto',)

        widgets = {
            'texto': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Escribe tu comentario '}),
        }
