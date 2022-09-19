from rest_framework import serializers
from .models import Student,Path

#1. yöntem
# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance
#2. yöntem
class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = ["id", "path_name"]
    
class StudentSerializer(serializers.ModelSerializer):
    # full_name=serializers.SerializerMethodField()
    # number_name=serializers.SerializerMethodField()

    # def get_full_name(self,obj):
    #     return f'{obj.first_name}{obj.last_name}'
    # def get_number_name(self,obj):
    #     return f'{obj.number}{obj.first_name}'
    path=serializers.StringRelatedField()
    path_id=serializers.IntegerField()
    class Meta:
        model = Student
        fields = ["id","path_id","path","first_name", "last_name", "number"]
        # fields = '__all__'
        # exclude = ['number']


# id ler auto icrement olarak verir django

##  string related yapinca read only olur. create yapamayiz.

## bu nedenle path_id integer field yaptik 

## path_id fs aws ve ds karsiligi 

## front end bizden sunu istedi. 
## mesela fs path ini sorgulayinca bunun icinde array olsun ve bu array icinde bu path e ait tüm ögrenciler gelsin 
## Student daki related _name kulanarak yapacagiz.
## bunun icin path serializer student inkinden sonra kullanilir. 
## path serializer icinde students diye alan olusturulur karsiliginda student serializer verilir. many true olmali. yani bir path altinda birden fazla object yani student döner
## ve path serialier in fields inda bu alan tanimlanir front end e gönderilir. 
## path serializer daki students ismi Student in serializer in daki related name ile ayni olmali. 






