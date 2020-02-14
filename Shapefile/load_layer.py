import os
from django.contrib.gis.utils import LayerMapping
from .models import Bara


# Auto-generated `LayerMapping` dictionary for bara model
Bara_mapping = {
    'objectid': 'OBJECTID',
    'palika': 'PALIKA',
    'district': 'DISTRICT',
    'gapa_napa': 'GAPA_NAPA',
    'gn_type': 'GN_TYPE',
    'province': 'PROVINCE',
    'geom': 'MULTIPOLYGON',
}

Bara_shp = os.path.abspath(os.path.join(os.path.dirname("_file_"),'data/Bara.shp'))

def run(verbose=True):
    lm = LayerMapping(Bara, Bara_shp, Bara_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
