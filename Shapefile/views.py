from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Bara, Shapefile
from osgeo import ogr  

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def Shape(request, shapefile, models=None):
    if(models==None):
        sucess = shapefile
        return render(request, "view.html", {'sucess':sucess})
    else:
        sucess = shapefile
        model = models
        return render(request, "palika.html" ,{'sucess':sucess,'model':model})

def Bara_datasets(request):
    bara = serialize('geojson',Bara.objects.all())
    return HttpResponse(bara, content_type='json')

def Shapefile_datasets(request):
    shapefile = serialize('geojson',Shapefile.objects.all())
    return HttpResponse(shapefile, content_type='json')

def to_geojson(request, shapefile, models=None):
    if (models==None): 
        sucess = serialize('geojson',Bara.objects.filter(gn_type=shapefile))
    else:
        sucess = serialize('geojson',Bara.objects.filter(gapa_napa=models))
    return HttpResponse(sucess, content_type='json')

    