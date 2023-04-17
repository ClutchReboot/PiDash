from rest_framework import views
from rest_framework.pagination import Response

from .serializers import *
from .utils import os_specs


class SysInfoView(views.APIView):

    def get(self, request, *args, **kwargs):
        data = [os_specs.os_specs()]
        results = SysInfoSerializer(data, many=True).data
        return Response(results)

