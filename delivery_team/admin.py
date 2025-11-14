from django.contrib import admin
from delivery_team.models import team
from delivery_team.models import service
from delivery_team.models import AirFreight
from delivery_team.models import OceanFreight
from delivery_team.models import LandTransport
from delivery_team.models import CargoStorage
from delivery_team.models import client

class teamAdmin(admin.ModelAdmin):
    list_display=('timg','tname')

class serviceAdmin(admin.ModelAdmin):
    list_display=('icon','name','info')

class AirFreightAdmin(admin.ModelAdmin):
    list_display=('img','srvname','srvheading','srvdetail','srvcontant')

class OceanFreightAdmin(admin.ModelAdmin):
    list_display=('img','srvname','srvheading','srvdetail','srvcontant')

class LandTransportAdmin(admin.ModelAdmin):
    list_display=('img','srvname','srvheading','srvdetail','srvcontant')

class CargoStorageAdmin(admin.ModelAdmin):
    list_display=('img','srvname','srvheading','srvdetail','srvcontant')

class clientAdmin(admin.ModelAdmin):
    list_display=('img','name','post','info')

admin.site.register(team,teamAdmin)
admin.site.register(service,serviceAdmin)
admin.site.register(AirFreight,AirFreightAdmin)
admin.site.register(OceanFreight,OceanFreightAdmin)
admin.site.register(LandTransport,LandTransportAdmin)
admin.site.register(CargoStorage,CargoStorageAdmin)
admin.site.register(client,clientAdmin)
# Register your models here.