import os
import requests
import tempfile

import geopandas as gpd
import networkx as nx
import osmnx as ox
import numpy as np
import peartree as pt
from shapely.geometry import Point

# Bay area rectangle select
tl_query = 'https://transit.land/api/v1/feeds?bbox=38.055199,-122.926353,37.252472,-121.672981'

# Brooklyn example rectangle select
# tl_query = 'https://transit.land/api/v1/feeds?bbox=-73.97339,40.649778,-73.946532,40.670353' 
header = {'apikey':'NMmVInTVH1ctN7deZOcDy2Wzbh53GVav'}

resp = requests.get(tl_query, headers=header)
rj = resp.json()
print(rj)

# zip_url = None
# for f in rj['feeds']:
#     if 'san francisco' in f['onestop_id']:
#         zip_url = f['url']