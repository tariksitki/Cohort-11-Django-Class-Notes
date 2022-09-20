from email.policy import HTTP
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


### class based imports:
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


# Create your views here.


            #### Func Based Views: (Bunlar bir önceki dersin view leri. Bu dersin class based view leri ise asagida)

def home(request):
    return HttpResponse('<h1>API Page</h1>')


# @api_view(['GET', 'POST'])
# def student_api(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def student_list(request):
#     students = Student.objects.all()
#     serializer = StudentSerializer(students, many=True)
#     # print(serializer.data)
#     return Response(serializer.data)


# @api_view(['POST'])
# def student_create(request):
#     print(request.data)
#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         data = {
#             "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"
#         }
#         return Response(data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def student_api_get_update_delete(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     if request.method == 'GET':
#         serializer = StudentSerializer(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": f"Student {student.last_name} updated successfully"
#             }
#             return Response(data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'PATCH':
#         serializer = StudentSerializer(
#             student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": f"Student {student.last_name} updated successfully"
#             }
#             return Response(data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         student.delete()
#         data = {
#             "message": f"Student {student.last_name} deleted successfully"
#         }
#         return Response(data)


# @api_view(['GET'])
# def student_detail(request, pk):
#     # try:
#     #     student = Student.objects.get(pk=pk)
#     # except Objdkdlşdş:
#     #     raise HTTP404
#     student = get_object_or_404(Student, pk=pk)
#     serializer = StudentSerializer(student)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['PUT'])
# def student_update(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     serializer = StudentSerializer(student, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         data = {
#             "message": f"Student {student.last_name} updated successfully"
#         }
#         return Response(data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PATCH'])
# def student_update_partial(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     serializer = StudentSerializer(student, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         data = {
#             "message": f"Student {student.last_name} updated successfully"
#         }
#         return Response(data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def student_delete(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     student.delete()
#     data = {
#         "message": f"Student {student.last_name} deleted successfully..."
#     }
#     return Response(data, status=status.HTTP_200_OK)


# @api_view(['GET', 'POST'])
# def path_api(request):
#     # from rest_framework.decorators import api_view
#     # from rest_framework.response import Response
#     # from rest_framework import status

#     if request.method == 'GET':
#         paths = Path.objects.all()
#         serializer = PathSerializer(
#             paths, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # from pprint import pprint
#         # pprint(request)
#         serializer = PathSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": f"Path saved successfully!"}
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










        ### Class Based View: 
        ## APIView e tiklayarak detayina bakalim.

class StudentList(APIView):
    ## request.method = "GET" in karsiligi asagidaki method:
    def get(self, request):  ## bunlar reserved isimler.
        students = Student.objects.all()
        ## birden fazla veri oldugu icin many true
        serializer = StudentSerializer(students, many=True)
        ## serializer dict bemzeri veri return eder dedi print diyerek bakalim
        return Response(serializer.data)

        ## bu methodu olusturduktan sonra browsable api de post secenegi gelir. yoksa gelmez.
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        ## serializer kendisi validation islemlerini yapar. Burada onu kullaniriz.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            ## else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    ## Update:

class StudentDetail(APIView):
        # bu method bize objectimizi getirir. diger methodlarda kullanilir bu method.
        # yani her method da ayri ayri objectimizi tekrardan yakalamak yerine hepsinde bu methodu cagiracagiz. 
    def get_obj(self, pk):  # reserved isim
        return get_object_or_404(Student, pk=pk)
        
    def get(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_data = serializer.data
            new_data["success"] = f"student {student.last_name} updated"
            return Response(new_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        ### delete de serializer a gerek yok.
    def delete(self, request, pk):
        student = self.get_obj(pk)
        student.delete()
        data = {
            "message" : f"student {student.last_name} deleted"
        }
        return Response(data, status=status.HTTP_200_OK)






    ## class Based Generic APIView: (mixin lerle beraber kullanilir.)
    ## önemli genericapiview en sagda olmali.
    ## buradan itibaren kod yükümüz azaliyor ama hakimiyetimiz azaliyor. 


        ## get ve post :
class StudentListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all() ## bu isim class in orijinalinde var
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) # get icin list

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) # post icin create




    ### update  read  delete:
    ## retrieve read demek,  destroy delete demek
    ## bunlar generic api view ile kullanilmak zorunda
    ## Biz class icinde methodlarin icinde ne islem yapilmasi gerektigini söyleyecegiz. Django kendisi herseyi otomatik yapacak. 

    ### Bu class in bir üsttekinden farki, üsttekinde sadece post ve get yapariz. Burada ise update delete islemleri ve get. Bu nedenle browser da otomatik cikan form icinde pk ile cagirdigimiz specific elemanin bilgileri gelir. ister sileriz ister degistiririz. 

class StudentURD(
    mixins.UpdateModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.DestroyModelMixin, 
    GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) ## get icin retrieve

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# hocam benim bildiğim list de bütün veriyi çekiyor
# retrieve de tek bir veri çekiyor
# yanlış bilgi aktarmış olmayayım hocam sinan hocama sorun siz yine de

## Not yukarida kullandigimiz tüm class lar APIView dan türetilmistir. 
## Normal apiview de uzun kodlar yazdik
# generic apiview de biraz azaldi. 
## concrete de ise iyice azalacak. 







##############  concrete API View: 
## üsttekilerde get ve post u manuel yazmistik . Burada artik herseyi dajngo yapar. 
## ListCreateAPIView nin nereden inherit edildigine bakalim. 

    ### post get

class StudentListCreateConcrete(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer




    ## retrieve delete update

class StudentRetUpDelConcrete(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer








            ### View Set:
        ### Burada ise concreteden daha kisa. burada iki method arasi ayrim yok. get update delete post hepsi tek yerde.

class StudentAllMethods(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    @action(detail=False, methods=["GET"])   #bu decorator dür.
    def student_count(self, request):
        count = {
            "student_count" : self.queryset.count()
        }
        return Response(count)

## action da olusturdugumuz count methodunu 
# http://127.0.0.1:8000/api/student/student_count/ 
# bu url ile kullanabiliyoruz 







