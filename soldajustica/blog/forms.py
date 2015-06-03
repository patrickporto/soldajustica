from django import forms
from suit_redactor.widgets import RedactorWidget


class PostForm(forms.ModelForm):
    class Meta:
        widgets = {
            'content': RedactorWidget(editor_options={'lang': 'pt-br'})
        }