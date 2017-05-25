from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.http import HttpResponse


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'healthcheck', lambda r: HttpResponse()),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
]
