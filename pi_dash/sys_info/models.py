from django.db import models


class SysInfo(models.Model):
    hostname = models.CharField(default='', max_length=100, unique=True)
    hostByHostname = models.CharField(default='', max_length=100, unique=True)
    hostByAddress = models.JSONField(default=dict, blank=True, max_length=200)
    localIpV4 = models.JSONField(default=dict, blank=True, max_length=200)
    platform = models.JSONField(default=dict, blank=True, max_length=200)
    latestUpdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hostname
