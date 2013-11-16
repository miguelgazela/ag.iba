from django.conf.urls import patterns, include, url

from app import views


urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'app/login.html'}),
)

