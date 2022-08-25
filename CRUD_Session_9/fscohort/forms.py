
from .models import Student
from django import forms

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__' 
        labels = {"first_name": "Adiniz", "last_name":"Soyadiniz", "number":"Numaraniz"}

