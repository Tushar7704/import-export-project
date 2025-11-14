from django.contrib import admin
from import_dyp.models import *

class hardwareAdmin(admin.ModelAdmin):
    list_display=('imimg','imtitle','imdtl')

class crudoilAdmin(admin.ModelAdmin):
    list_display=('imimg','imtitle','imdtl')

class motorAdmin(admin.ModelAdmin):
    list_display=('imimg','imtitle','imdtl')

class motorsplAdmin(admin.ModelAdmin):
    list_display=('imimg','imtitle','imdtl')

class mechanicalAdmin(admin.ModelAdmin):
    list_display=('imimg','imtitle','imdtl')

admin.site.register(hardware,hardwareAdmin)
admin.site.register(crudoil,crudoilAdmin)
admin.site.register(motor,motorAdmin)
admin.site.register(motorspl,motorsplAdmin)
admin.site.register(mechanical,mechanicalAdmin)
# Register your models here.