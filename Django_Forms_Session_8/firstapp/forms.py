
from django import forms
from .models import Student


    ### manuel

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     number = forms.IntegerField(required=False)
#     profile_image = forms.ImageField(required=False)


### biz formu bu sekilde olusturup template de cektik ama browser da inspect i acarsak tüm kodlarimizi normal htm for kodlarina cevirdigini görürüz. 



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "number", "profile_pic"]
        labels = {"first_name": "Name"}  ## label ismi degisikligi

## fields = "__all__" da kullanabiliriz
## buna dunder score denir.  double under score dan gelir. 

