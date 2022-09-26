from django.db import models

# Create your models here.

    ## abstract model.  tekrar eden seyler icin kullanilir. db de ve admin panel de görünmez. kendi kodumuzda kullanilir. bu zaten models dan inherit edildigi icin bunu kullanan tablolarda buna sahip olur. Bunu kullanan tablollarin inherit yerine bunu kullaniyoruz. 
class UpdateCreateDate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    ## parent tablo
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Category Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    ## bu tablo quiz ile ilskil o nedenle bu category de kac quiz oldugunu user a gösterebiliirz. Bunu serializers da da isleme alacagiz. self.quizz dedigimizde direkt child model icine girebiliyoruz ve orada ki herseye ulasabiliyoruz. eger related name kullanmazsak quiz_set  demek zorundayiz.deneyelim Burada kural Quiz modelinin isminin kücük hali ve set arada ise _  kullanilir. related name daha human redable isim yapar. 
    @property
    def quiz_count(self):
        return self.quizz.count  ## child tabloda related_name

## verbose name plural neden kullanilir:  Bu tablomuzun adi Category,  db de ise sonuna -s gelir. ama normalde -ies olmasi lazim. O nedenle kullanilir. 




    ## child tablo:

# class Quiz(models.Model):  ## abstract kullandigimiz icin bunu comment
class Quiz(UpdateCreateDate):
    title = models.CharField(max_length=50, verbose_name="Quiz Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="quizz") ## category silindiginde sorularda silinsin diyoruz.
    # created = models.DateTimeField(auto_now_add=True) ## bunlar yerine abstractan 
    # updated = models.DateTimeField(auto_now=True)

    @property   ## bu kez related name yazmadik. diger kurali kullandik. 
    def question_count(self):
        return self.question_set.count  # bu isim kural question_set
    ## property kullanmazsak count in sonuna () gerek yok. normal de method oldugu icin var

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Quizzes"




class Question(models.Model):
    SCALE = (
        ("B", "Beginner"),  ## ilk parametre db icin
        ("I", "Intermediate"),
        ("A", "Advanced"),
    )
    title = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    difficulty = models.CharField(max_length=1, choices=SCALE)

    def __str__(self):
        return self.title

    ## answers:
class Options(models.Model):
    option_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options") ## bunu question icine gömecegiz. serializer da. bunun yerine options_set denebilir. 
    is_right = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.option_text






## difficulty icin bir select box olusturup user in secmesini saglayabiliriz. 
# degerler degismeyecek ise hareketli degil ise yukaridaki gigi tuple kullanilir. 

## abstract class i sürekli tekrar eden seyler icin kullanilir. mesela update_date in kodu gibi. bunlari kesisim kümesi gibi bir yerde toplayip oradan import etme 

## cascade yerine set null dersek null true demek zorundayiz. 
## category silindiginde sorular baska bir category e tasinsin diyebiliirz. Bunun icin algoritma yazmayi deneyelim . 
## teachers diye tablo olusturabiliriz. hangi soruyu hangi teacher hazirlamis onu tutabiliriz. 


## user admin de tek tek her tabloya gidip veri girmekle ugrasmasin diye bütün cerileri tek bir sayfada toplayip user in isini kolaylastirmak istiyoruz. bunun icin admin panel de iliskili tablolari nested sekilde birbiri icine yerlestirecek yapi bulunur. 
## django nested admin  bunun docs u var.  orada hersey yaziyor. 

# https://django-nested-admin.readthedocs.io/en/latest/quickstart.html


## db ye yeni field ekledigimizde, eskiden o tabloda o veri olmadigi icin onun yerine birsey atamamizi ister. 