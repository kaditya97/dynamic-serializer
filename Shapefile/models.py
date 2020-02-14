
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.gdal import DataSource



# Create your models here.
class Shapefile(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)

    @property
    def lat_lan(self):
        return list(getattr(self.location, 'coords', [])[::-1])


    class Meta:
        verbose_name_plural = "Shapefile"

    def __str__(self):
        return self.name

class Bara(models.Model):
    objectid = models.BigIntegerField()
    palika = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    gapa_napa = models.CharField(max_length=50)
    gn_type = models.CharField(max_length=50)
    province = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.palika

    class Meta:
        verbose_name_plural = "Bara"

class Test(models.Model):
    title = models.CharField(max_length=20)
    descrption = models.CharField(max_length=20)

class Meta:
    verbose_name_plural = "Test"