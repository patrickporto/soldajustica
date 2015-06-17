from django import forms
from suit_redactor.widgets import RedactorWidget
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'author',
            'content',
            'published',
        )
        widgets = {
            'content': RedactorWidget(editor_options={'lang': 'pt-br'})
        }