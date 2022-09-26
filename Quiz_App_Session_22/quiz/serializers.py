
from dataclasses import field, fields
from rest_framework import serializers
from .models import Options, Category, Question, Quiz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'quiz_count'  ## bunu models de düzenledik. 
        )


class QuizSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'category',
            'question_count'
        )

### stringrelateddield str d ne varsa onu döner 






class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = (  ## question icine gömecegiz o nedenle question filed i yok
            "id",
            "option_text",
            "is_right",
        )



class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many = True)
    quiz = serializers.StringRelatedField()
    
    class Meta:
        model = Question
        fields = (
            "id",
            "title",  ## bu sorular. sorularin altinda da cevaplar yani options
            "options",
            "difficulty"
        )





# reverse relation   child dan parent a iliskidir. Bunun icin related name kullanmak daha iyi bir yöntem