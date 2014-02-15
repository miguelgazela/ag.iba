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
    url(r'^impostos/novo/(?P<client_id>\d+)$', views.add_tax, name="add_tax"),
    url(r'^impostos/(?P<sort>[a-z]+)/$', views.taxes, name="taxes"),
    url(r'^impostos/remover/(?P<tax_id>\d+)$', views.remove_tax, name="remove_tax"),

    # clients urls
    url(r'^clientes$', views.clients, name="clients"),
    url(r'^clientes/(?P<sort>[a-z]+)/$', views.clients, name="clients"),
    url(r'^clientes/(?P<client_id>\d+)$', views.client, name="client"),
    url(r'^clientes/novo$', views.add_client, name="add_client"),
    url(r'^clientes/remover/(?P<client_id>\d+)$', views.remove_client, name="remove_client"),

    # api urls
    url(r'^api/impostos/pagar/(?P<tax_id>\d+)$', views.pay_tax, name="pay_tax"),
    url(r'^api/impostos/cancelar/(?P<tax_id>\d+)$', views.cancel_tax, name="cancel_tax"),
)

