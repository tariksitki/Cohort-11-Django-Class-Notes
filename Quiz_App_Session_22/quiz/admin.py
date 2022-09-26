from django.contrib import admin

# Register your models here.

from .models import Category, Options, Question, Quiz
## nested admin
import nested_admin  #########  Önemli

#     ## en alttan en üste dogru gidiyoruz. en asagidaki tablo nihai nokta
# class OptionAdmin(nested_admin.NestedTabularInline):
#     model = Options 


# class QuestionAdmin(nested_admin.NestedTabularInline):
#     model = Question
#     inlines = [OptionAdmin]


# class QuizAdmin(nested_admin.NestedModelAdmin):  ## burada inherit farkli dikkkat
#     model = Quiz
#     inlines = [QuestionAdmin]
#     ## en son bu tabloyu da alip Quiz in register inin yanina koyariz. 


    ## yukaridaki kod hata vermisti. 

    # nested yapida category koymadik. cünkü quiz girerken girebiliiz category. 
class OptionAdmin(nested_admin.NestedTabularInline):
    model = Options
    extra = 5


class QuestionAdmin(nested_admin.NestedTabularInline):
    model = Question
    inlines = [OptionAdmin]
    extra = 5 ## hazir olarak 5 tane eklesin
    max_num = 20  ## en fazla 25 question ekleyebiliriz. 


class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionAdmin]


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Options)


# burada olusturdugumuz yapiya;  quizzes tablosunda add dedigimizde ulasiriz. 
## Biz bu sekilde verilerimizi girdigimizde alt tablolara gittigimizde orada da verilerin olustugunu görecegiz. 
#  müşteri geldi dedi ki ben admin panele girdiğimde tek bir yerde quizin kategorisini, quizin başlığını,quizin sorularını ve cevaplarını tek bir yerden girebileyim dedi.bizde developer olarak admin paneli müşterinin isteğine göre customize ediyoruz gibi düşünebilirsiniz
