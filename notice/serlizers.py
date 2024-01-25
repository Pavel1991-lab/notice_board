from rest_framework import serializers
from notice.models import Notice

from fidback.serlizers import FidbackSerlizer


# from lesson.validators import LessonValidator


class NoticeSerlizer(serializers.ModelSerializer):
    all_fidback = serializers.IntegerField(read_only=True, source='fidback_set.all.count')
    fidback = FidbackSerlizer(source='fidback_set', many=True, read_only=True)
    class Meta:
        model = Notice
        fields = '__all__'
