from django.contrib import admin
from django.urls import path, re_path,include
from django.views.static import serve
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('web.urls'), name='web'),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_FILE_ROOT}),
]
