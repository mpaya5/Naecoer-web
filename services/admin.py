from django.contrib import admin
from .models import Service
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class ServiceAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Service, ServiceAdmin)