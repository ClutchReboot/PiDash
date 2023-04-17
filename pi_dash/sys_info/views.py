from rest_framework import views
from rest_framework.pagination import Response

from .serializers import *
from .utils import get_sys_info


class SysInfoView(views.APIView):

    def get(self, request, *args, **kwargs):
        data = [get_sys_info()]
        results = SysInfoSerializer(data, many=True).data
        return Response(results)

