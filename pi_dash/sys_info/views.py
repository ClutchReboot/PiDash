from rest_framework import viewsets,  mixins
from rest_framework.pagination import LimitOffsetPagination, Response

from .serializers import *  # Importing .models from here
from .utils import os_specs


class SysInfoViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = SysInfo.objects.all()
    serializer_class = SysInfoSerializer
    pagination_class = LimitOffsetPagination

    def _build_os_specs(self):
        data = os_specs.os_specs()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return self.filter_queryset(self.get_queryset())

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        if not queryset:
            queryset = self._build_os_specs()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = SysInfoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SysInfoSerializer(queryset, many=True)
        return Response(serializer.data)
