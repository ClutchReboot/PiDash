from rest_framework import serializers


class SysInfoSerializer(serializers.Serializer):
    hostname = serializers.CharField()
    hostByHostname = serializers.CharField()
    hostByAddress = serializers.ListField()
    localIpV4 = serializers.JSONField()
    platform = serializers.JSONField()
