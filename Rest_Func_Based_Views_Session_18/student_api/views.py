from functools import partial
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student,Path

from .serializers import StudentSerializer,PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


## Önemli:  put patch get update methodlarinin hepsi icin sadece tek bir method yazilir ve tek bir endpoint yapilir. gelen istege göre user a dönüs yapilir. Ama biz burada daha iyi anlayalim diye asagida hepsini tek tek olarak da yazdik 

## tek tek method yazip tek tek url yazmak uygun degil. tek method da gelen istege göre if ile islemler yaptirilir. 


def home(request):
    return HttpResponse('<h1>API Page</h1>')


## buradaki decorator u yazdigimiz icin browsable api i görürürz django template inde.
@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)




@api_view(['GET', 'POST'])
def path_api(request):
    # from rest_framework.decorators import api_view
    # from rest_framework.response import Response
    # from rest_framework import status

    if request.method == 'GET':
        paths = Path.objects.all()
        serializer = PathSerializer(paths, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        # from pprint import pprint
        # pprint(request)
        serializer = PathSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Path saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




## rest de istek sayimiz artar. patch put gibi

# Response metodu isteğin nereden geldiğini anlıyor

            ## Simdi get ile POST u ayri ayri yazacagiz. yukarida birlesik. best practice birlesik 
            #### GET:

## db den veri cekiyoruz json a ceviriyoruz ve response olarak döneriz. 
## Bu view icin ayri bir url verdik. 
## burada sadece GET yazdigimiz icin post icin bir  görüntü gelmez. Burada POST yazip algoritmasini yazmazsak, sadece görüntüsü gelir. tusa basinca islem yapmaz. 
# burada sadece fs cohorta ait student lari isteseydik. Student.objects.filter(path=1)
## bunu bir tusa basinca nasil yapariz? 
@api_view(["GET"]) # bu decorator vasitasi ile arayüz gelir. yoksa gelmez. 
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True) # json lastirmak icin kullanilir. buradaki degisken ismi degisebilir
    # print(serializer) # yukarida tanimlanan serializers in kendisini verir. 
    # print(serializer.data)
    return Response(serializer.data) # json datasina bu sekilde ulasilir. 


## decorator yazmadan postman de data lari görmek icin @csrf_exempt






            ### POST.
            ## az önce db den veri cekiyorduk. simdi ise frontend den gelen datayi serializer icine koyup db ye gönderecegiz. yani tersine islem
            # django template kisminda datayi request.POST ile cekiyorduk burada reuqest.data 
            ## Burada front end e response vermiyoruz. onlardan alinan veriyi db ye kaydediyoruz. Bu nedenle burada response icine sadece mesaj konulur. 
            # path i string related yaptik., Bu nedenle read only oldu. o nedenle create ederken bunu yazamayiz. Bunun yerine path_id yazariz. 

@api_view(["POST"])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    print(request.data) ## dict formartinda gelir bize. Biz bunu seria ile django nun anlayacagi bir dile ceviriyoruz. 
    if serializer.is_valid():
        serializer.save()
        data = {
            "message" : "Student created succesfully..."
        }
        return Response(data, status = status.HTTP_201_CREATED)
        ##else
    return Response(serializer.errors)

## postman de get yapilacagi zaman body kullanmay gerek yok. post isleminde kullaniriz. 

# postman de tek tirnak hata verir  "" kullanalim 






        ### DETAIL GET:
        ## django geri planda hep pk kullanir. pk genel bir kavramdir.Bu nedenl ebiz de id yerine bunu kullanirak daha iyi olur. 
        ## detail e ulasmak icin db den önce o object i cekmemiz gerekir. 

        ## front end den istek geldi ve pk gönderdiler. Bu pk ya göre db den object imizi bulduk cektik. Bunu serializer ile json a dönüstürdük ve tekrar front end e gönderdik. 
@api_view(["GET"]) 
def student_detail(request, pk):
    # student = Student.objects.get(pk=pk) # bu yöntemde eger bulamazsa hemen hata verir
    student = get_object_or_404(Student, pk=pk) # db den veri cekmenin diger yolu. Burada Student tablomuzun ismi,  virgülden sonrasi ise kosul.. Bu bir func dir. ve hem saglam calisma secenegi hem de hata ihtimalini ele alir. http404 hatasi bir not found hatasidir ve cover edilebilir bir hatadir. Bu yöntemi kullanmasak try except kullanmamiz gerekirdi. 
    serializer = StudentSerializer(student) # burada tek bir object dönecek. many true yok
    return Response(serializer.data, status=status.HTTP_200_OK)







        ### Update:
        ## burada da single object alip onun üzerinde islem yapacagiz.
        # ## forms da instance vardi. Burada ise data 
        ## bu put islemi. burada tüm veri gönderilmek zorunda tek alan degistiirlmek istense bile. 
        ## patch de ise sadece degistirmke istedigimiz alani göndermemiz yeterli. 

@api_view(["PUT"])
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            "message": f"{student.last_name} updated succesfully..."
        }
        return Response(data, status=status.HTTP_200_OK)
        ## else,
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





            ### patch:
            ## sadece degistirmek istedigimiz alani gireriz. 
@api_view(["PATCH"])
def student_update_partial(request, pk):
    student = get_object_or_404(Student, pk=pk)
    serializer = StudentSerializer(student, data=request.data, partial=True) ## *****
    if serializer.is_valid():
        serializer.save()
        data = {
            "message": f"{student.last_name} updated succesfully..."
        }
        return Response(data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






        ### delete:
        ## burada serializer ile isimiz yok. direkt silme 
    ## bunun url ini browser a yazdigimizda bize HTTP 405 Method Not Allowed diye bir yazi cikar. Buna ragmen delete tusuna basinca siler o elemani. 
    # postman de bunun icin de body e birsey koymaya gerek yok. sadece url yazmamiz ve url sonuna silinecek id yazmamiz yeterli. 

@api_view(["DELETE"])
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    data = {
        "message": f"{student.last_name} deleted succesfully..."
    }
    return Response(data, status=status.HTTP_200_OK)




## postman de sag taraf da bize front end kodu da verilir. 
## sag taraf da code isareti var. 