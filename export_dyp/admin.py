from django.contrib import admin
from export_dyp.models import *

class ExportProductAdmin(admin.ModelAdmin):
    list_display=('extitle','eximg','exdesc')

admin.site.register(ExportProduct,ExportProductAdmin)
# Register your models here.