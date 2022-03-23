from django.contrib import admin
from .models import Studies

# Register your models here.

class StudiesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id','title')

admin.site.register(Studies, StudiesAdmin)
