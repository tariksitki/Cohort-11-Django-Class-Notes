from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from quiz.serializers import CategorySerializer, QuestionSerializer, QuizSerializer
from .models import Options, Category, Question, Quiz

from django_filters.rest_framework import DjangoFilterBackend

### search filter
from rest_framework import filters

    ## category leri api seklinde json formatinda gönderme
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    ## frontend e gönderme 
class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]  ## bu category nin id sine göre filtreleme yapar.   
    # filterset_fields = ["category__name"]  
    ## neye göre filtreleme yapacagim. filters diye bir tus gelir. 
    ## child dan parent a ulasmak icin __ kullanilir. yani buradan Category tablosundaki name e ulasiyoruz ve ona göre filtreleme yapiyoruz. 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["title"] ## filters dan sonra filter butonu cikar. 


## backend e tikladigimizda json veri de sadece backend e ait quizler gelsin istersek django filter kullaniriz.  pip install django-filter sonra settings e ekleme.  


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["quiz", "difficulty"] ## question tablosundaki quiz e göre filtreleme 


## https://anthony67-react-drf-quizapp.vercel.app/



