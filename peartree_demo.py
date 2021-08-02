import os
import requests
import tempfile

import geopandas as gpd
import networkx as nx
import osmnx as ox
import numpy as np
import peartree as pt
from shapely.geometry import Point

tl_query = 'https://transit.land/api/v1/feeds?bbox=-73.97339,40.649778,-73.946532,40.670353'

resp = requests.get(tl_query)
rj = resp.json()

zip_url = None
for f in rj['feeds']:
    if 'oakland' in f['onestop_id']:
        zip_url = f['url']