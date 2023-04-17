from .views import SysInfoView

from django.urls import path
from django.views.generic.base import TemplateView


urlpatterns = [
    path('home/', TemplateView.as_view(template_name='si_home.html'), name='si_home'),
    path('api/sys_info/', SysInfoView.as_view(), name='sys_info')
]
