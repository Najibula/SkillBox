from django import forms
from django.core.exceptions import  ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile

class UserBioForm(forms.Form):
    name = forms.CharField(max_length=40)
    id = forms.IntegerField(label="Age", min_value=14, max_value=60)
    bio = forms.CharField(label="Biography",widget=forms.Textarea)

def validate_file_name(file:InMemoryUploadedFile) -> None:
    if file.name and "virus" in file.name and "Gitlab" in file.name:
        raise ValidationError("поменяй пож. имя файла без 'virus's")

class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[validate_file_name])