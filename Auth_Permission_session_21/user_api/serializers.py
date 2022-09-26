

## register icin:
## Bu serializer i model serializerdan yazabilirdik ama bu güzel. daha sonra da kullanabiliriz. 


from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,  # normalde zorunlu degil biz yaptik 
            validators=[UniqueValidator(queryset=User.objects.all())]
            )  #ayni emaili baska user kullanamasin 

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])   # sadece yazilir geriye döndürülmez. validation demek 6  8  karakter olacak felan 
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):    ## custom validation. password2 yanlissa hata mesaji
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

        ## create methodu yeniden tanimladik. passwordu burada cretae edemeyiz. cünkü db ye acik bir sekilde yazilirdi. hashlensin diye biz daha sonra setpassword methodu kullaniriz. 
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
            ## hashlensin diye. 
        user.set_password(validated_data['password'])
        user.save()

        return user


        ### simdi reister icinn view  yazariz. 

## yeni user create etmek icin su bilgiler lazim 

# {
#     "username": "Henry",
#     "password": "Murtaza66",
#     "password2" : "Murtaza66",
#     "email" : "test@test.com",
#     "first_name" : "henry",
#     "last_name" : "forester"

# }