from django.conf.urls import patterns, include, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),

    # auth urls
    url(r'^login$', views.login, name="login"),
    url(r'^signup$', views.signup, name="signup"),
    url(r'^logout$', views.logout, name="logout"),

    # taxes urls
    url(r'^impostos$', views.taxes, name="taxes"),
    url(r'^impostos/novo$', views.add_tax, name="add_tax"),
    url(r'^imposts/(?P<sort>[a-z]{1,})/$', views.taxes, name="taxes"),

    # clients urls
    url(r'^clientes$', views.clients, name="clients"),
    url(r'^clientes/(?P<sort>[a-z]{1,})/$', views.clients, name="clients"),
    url(r'^clientes/(?P<client_id>\d+)$', views.client, name="client"),
    url(r'^clientes/novo$', views.add_client, name="add_client"),
)

