from rest_framework import serializers
from .models import SysInfo


class SysInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SysInfo
        fields = '__all__'
