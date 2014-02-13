from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('app.urls')),
    url(r'^agiba/', include('app.urls')),
    url(r'^agiba/admin/', include(admin.site.urls)),
)
