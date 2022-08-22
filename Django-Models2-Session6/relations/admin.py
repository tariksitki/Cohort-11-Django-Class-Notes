from django.contrib import admin

from relations.models import Creator, Framework, Language

# Register your models here.

admin.site.register(Language)
admin.site.register(Creator)
admin.site.register(Framework)