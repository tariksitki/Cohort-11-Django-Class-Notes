from django.shortcuts import render, redirect
from fscohort.forms import StudentForm

from fscohort.models import Student

# Create your views here.


def index(request):
    return render(request, "fscohort/index.html")


def student_list(request):
    students = Student.objects.all()
    print(students)

    context = {
        "students" : students
    }
    return render(request, "fscohort/student_list.html", context)
    # context direkt parantez icine de yazilabilir.



def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")  # Önemli: redirect den önce return


    context = {
        "form" : form
    }
    return render(request, "fscohort/student_add.html", context)





def student_update(request, id):
    student = Student.objects.get(id = id)
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")

    context = {
        "form" : form
    }
    return render(request, "fscohort/student_update.html", context)

## object ile instance arasindaki fark:  object kalıp, instance kalıptan yapılan nesne
# eger object den bir örnek üretmezsek kalip olarak kalir

## db de her bir satir record



def student_delete(request, id):
    student = Student.objects.get(id=id)   # filter ile deneyelim  # 1. id django       tarafindan otomatik üretilen alan. 2. ise bizim parametre olarak verdigimiz
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    context = {
        "student" : student
    }

    return render(request, "fscohort/student_delete.html", context)


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'fscohort/student_detail.html', context)


