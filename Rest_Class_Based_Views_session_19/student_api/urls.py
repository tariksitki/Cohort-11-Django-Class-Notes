
from django.urls import path, include
from .views import (

        ### func based
    StudentAllMethods,
    StudentDetail,
    StudentListCreate,
    StudentListCreateConcrete,
    StudentRetUpDelConcrete,
    StudentURD,
    home,
    # student_api,
    # student_api_get_update_delete, path_api,
    # student_list,
    # student_create,
    # student_detail,
    # student_update,
    # student_update_partial,
    # student_delete

        ## class based
    StudentList,
    
)
    ### views.py in sonundaki viewsets ler icin bunu kullandik. 
from rest_framework import routers #? 1. 👈 For ViewSet APIView
router = routers.DefaultRouter()    #? 2. 👈 For iewSet APIView
router.register('student', StudentAllMethods) #? 3. 👈  For ViewSet APIView



        ## Func based views  urls:
# urlpatterns = [
    # path('', home),
#     path('student/', student_api),
#     path('student/<int:pk>/', student_api_get_update_delete, name="detail"),
#     path('path/', path_api),
#     path('student_list/', student_list, name='student_list'),
#     path('student_create/', student_create, name='student_create'),
#     path('student_detail/<int:pk>/', student_detail, name='student_detail'),
#     path('student_update/<int:pk>/', student_update, name='student_update'),
#     path('student_update_partial/<int:pk>/',
#          student_update_partial, name='student_update_partial'),
#     path('student_delete/<int:pk>/', student_delete, name='student_delete'),

# ]




    ## class based views  urls:
    # Bazilarinda ayni url i kullandik o nedenle yoruma aldik. 

urlpatterns = [
    path('', home),
    # path("student/", StudentList.as_view(), name="student"),
    # path("student_detail/<int:pk>/", StudentDetail.as_view(), name="student_detail"),
    # path("student/", StudentListCreate.as_view(), name="student"),
    # path("student/<int:pk>/", StudentURD.as_view(), name="student"),
    # path("student/", StudentListCreateConcrete.as_view(), name="student_list"),
    # path("student/<int:pk>/", StudentRetUpDelConcrete.as_view(), name="student_retrieve"),

        ## viewsets: 
        ## endpoint olarak student yazarsak hepsi gelir. student/1 yazarsak specific
    path('', include(router.urls)) #? 4. 👈  For ViewSet APIView

]






# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'students', StudentCRUD, basename='student')
# urlpatterns = router.urls