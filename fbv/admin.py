from django.contrib import admin

from fbv.models import Countries, People

# Register your models here.
admin.site.register(People)
admin.site.register(Countries)