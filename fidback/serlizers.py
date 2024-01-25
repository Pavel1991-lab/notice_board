from rest_framework import serializers
from fidback.models import Fidback


# from lesson.validators import LessonValidator


class FidbackSerlizer(serializers.ModelSerializer):

    class Meta:
        model = Fidback
        fields = '__all__'
