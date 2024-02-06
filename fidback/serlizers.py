from rest_framework import serializers
from fidback.models import Fidback


class FidbackSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Fidback
        fields = '__all__'
