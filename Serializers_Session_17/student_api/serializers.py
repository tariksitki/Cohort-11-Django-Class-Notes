
from rest_framework import serializers
from .models import Path, Student

## serializers valiation islemini kendisi gerceklestirir. 
#   **    keywordarguments demek. burada key value ciftlerini acmak icin kullanilir. 

### django db ye veri kaydedeerken id yi otomatik kendisi üretir. Bu nedenle post isleminde user dan id istemiyoruz. 

## browsable api de post yaparken id girersek bunu dikkate almiyor. kendisi siraya göre id atamasi yapiyor. 

        ### normal serializer
        ## burada id alani yazmadigimiz icin gelmez. ama asagidaki model de kullandik. 

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)
#     ## null true ve blank true db yi ilgilendirir. Burada ise required. yani db de null burada required
    
#     ## hoca create ve update methodlari olusturulmak zorunda dedi. bakalim

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance

## Browsable api bize post imkani da verir. Cünkü view imizda post da yazdik.








            ### Model Serializer:
            ## burada create update yazmiyoruz. herseyi kendi yapiyor. 

class StudentSerializer(serializers.ModelSerializer):
    ## islemle elde edilebilecek verileri db ye kaydetmiyoruz. burada da fullname i islem ile elde edebiliyoruz. get_full_name isimli methodu kullanabilmek icin su kodu yazmamiz gerekir. 
    ## önemli method ismi ile buradaki isim ayni olmak zorunda ve bu degiskenin ismi fields da olamk zorunda. 
    full_name = serializers.SerializerMethodField()
    number_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    def get_number_name(self, obj):
        return f"{obj.number} {obj.last_name}"

    class Meta:
        model = Student
        fields = ["id", "full_name","number_name", "first_name", "last_name", "number"]
        # fields = '__all__'
        # exclude = ['number']

## serializerMethodField şu işi yapar:
## ben aynı isimde bir function tanımlıcam. ondaki return değerini al, bu attribute'ye ata.
## https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield











        ######### telational:

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = ["id", "path_name"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"