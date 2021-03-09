
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


class SearchBookForm(forms.Form):
    title = forms.CharField(label = 'mon titre', max_length = 100)