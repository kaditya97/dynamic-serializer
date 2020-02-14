
from django.contrib import admin
from django.contrib.gis import admin
# Register your models here.
from .models import Shapefile, Bara, Test

class ShapefileAdmin(admin.GeoModelAdmin):
    list_display=('name','location')

class BaraAdmin(admin.GeoModelAdmin):
    list_display = ('palika','province','gapa_napa','gn_type')

admin.site.register(Shapefile, ShapefileAdmin)
admin.site.register(Bara, BaraAdmin)
admin.site.register(Test)