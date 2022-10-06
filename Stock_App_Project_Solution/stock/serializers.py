
from rest_framework import serializers
from .models import (
    Category,
    Brand,
    Firm,
    Transaction,
    Product
)




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name"
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "",
            ""
        )




## product tablosu ile category tablolar bagli ama biz string degerlrini almak istersek string related field kulanbilir. 

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField(write_only=True)
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product 
        fields = (
            "id",
            "category",
            "category_id",
            "brand",
            "brand_id",
            "stock",
        )

        read_only_fields = ("stock",)  ## yada yukarida bir degiskene atayarak parantez icinde read_only yazabilirdik. bunu neden yaprik. transactionda gelen quantity ye göre update olmasini istiyoruz. create ederken olussun istemiyoruz. 






class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            "id",
            "name",
            "phone",
            "address",
        )




## Transaction modleine gittigimizde 3 tane foreign key li alan vardir. 
## user i o andaki user kim ise oradan alacagiz

### transaction "in" ise bunu models de handle etmistik. Burada ise out u handle edecegiz. 
   
            


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    firm = serializers.StringRelatedField()
    firm_id = serializers.IntegerField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()

    class Meta:
        model = Transaction
        fields = (
            'id',
            'user',
            'firm',
            'firm_id',
            'transaction',
            'product',
            'product_id',
            'quantity',
            'price',
            'price_total'
        )

        read_only_fields = ('price_total',)

    def validate(self, data):
        if data.get('transaction') == 0:
            ## burada data dedigimiz fields icinde yazdigimiz alanlar ile gelen veri
            product = Product.objects.get(id=data.get('product_id'))
            ## eger stock dakinden fazla satmak istersek.
            if data.get('quantity') > product.stock:
                raise serializers.ValidationError(
                    f'Dont have enough stock. Current stock is {product.stock}'
                )
        return data
