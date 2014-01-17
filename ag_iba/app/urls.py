from django.conf.urls import patterns, include, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),

    # auth urls
    url(r'^login$', views.login, name="login"),
    url(r'^signup$', views.signup, name="signup"),
    url(r'^logout$', views.logout, name="logout"),

    # taxes urls
    url(r'^taxes$', views.taxes, name="taxes"),
    url(r'^taxes/(?P<sort>[a-z]{1,})/$', views.taxes, name="taxes"),
)

