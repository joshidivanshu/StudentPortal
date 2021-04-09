from django import forms
from .models import Teacher


class TeacherRegistration(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['eno','name','email','subject','experience']
        widgets = {
            'eno': forms.TextInput(attrs={'class': 'form-control', 'id': 'enoid'}),
            'name':forms.TextInput(attrs={'class':'form-control','id':'nameid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'id': 'subjectid'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'id': 'experienceid'}),
        }