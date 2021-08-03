import os
import requests
import tempfile

import geopandas as gpd
import networkx as nx
import osmnx as ox
import numpy as np
import peartree as pt
from shapely.geometry import Point
import pprint

# Bay area rectangle select
tl_query = 'https://transit.land/api/v1/operators?bbox=-122.503607,37.166611,-121.713958,38.038060'

# Brooklyn example rectangle select
# tl_query = 'https://transit.land/api/v1/stops?bbox=-73.97339,40.649778,-73.946532,40.670353' 

header = {'apikey':'NMmVInTVH1ctN7deZOcDy2Wzbh53GVav'}

resp = requests.get(tl_query, headers=header)
rj = resp.json()
pprint.pprint(rj['stops'][10])

# zip_url = None
# for f in rj['feeds']:
#     if 'san francisco' in f['onestop_id']:
#         zip_url = f['url']