from .views import SysInfoViewSet
from rest_framework.routers import DefaultRouter

from django.urls import include, path
from django.views.generic.base import TemplateView

api_router = DefaultRouter()
api_router.register('sys_info', SysInfoViewSet, basename='sys_info')

urlpatterns = [
    path('home/', TemplateView.as_view(template_name='si_home.html'), name='si_home'),
    path('api/', include(api_router.urls)),
]
