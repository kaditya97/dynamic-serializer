from django.conf.urls import include,url
from .views import HomePageView, Bara_datasets, Shapefile_datasets,Shape, to_geojson


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name = 'home'),
    url(r'^Shape/(?P<shapefile>\w+)/$', Shape, name = 'Shape_data'),
    url(r'^Shape/(?P<shapefile>\w+)/(?P<models>\w+)/$', Shape, name = 'Shape_data'),
    url(r'^Bara_data/$', Bara_datasets, name = 'Bara'),
    url(r'^api/(?P<shapefile>\w+)/$', to_geojson, name='geojson'),
    url(r'^api/(?P<shapefile>\w+)/(?P<models>\w+)/$', to_geojson, name='geojson'),
    url(r'^Shape_data/$', Shapefile_datasets, name = 'Shape'),
]