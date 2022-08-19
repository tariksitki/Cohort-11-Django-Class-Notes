
from rest_framework import serializers

from firstApp.models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink()
        fields = ["id", "name", "description"]

