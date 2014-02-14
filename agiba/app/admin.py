from django.contrib import admin
from app.models import Client
from app.models import Tax

class ClientAdmin(admin.ModelAdmin):
    pass

class TaxAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)
admin.site.register(Tax, TaxAdmin)