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
tl_query_ops = 'https://transit.land/api/v1/operators?bbox=-122.503607,37.166611,-121.713958,38.038060'
tl_query_routes = 'https://transit.land/api/v1/routes?bbox=-122.503607,37.166611,-121.713958,38.038060'
tl_query_stops = 'https://transit.land/api/v1/stops?bbox=-122.503607,37.166611,-121.713958,38.038060'
tl_query_feeds = 'https://transit.land/api/v1/feeds?bbox=-122.503607,37.166611,-121.713958,38.038060'

# Brooklyn example rectangle select
# tl_query = 'https://transit.land/api/v1/stops?bbox=-73.97339,40.649778,-73.946532,40.670353' 

header = {'apikey':'NMmVInTVH1ctN7deZOcDy2Wzbh53GVav'}

resp_ops = requests.get(tl_query_ops, headers=header)
resp_routes = requests.get(tl_query_routes, headers=header)
resp_stops = requests.get(tl_query_stops, headers=header)
resp_feeds = requests.get(tl_query_feeds, headers=header)

rj_ops = resp_ops.json()
rj_routes = resp_routes.json()
rj_stops = resp_stops.json()
rj_feeds = resp_feeds.json()

# pprint.pprint(rj_ops['operators'][0])
# pprint.pprint(rj_routes['routes'][0])
pprint.pprint(len(rj_stops['stops']))
pprint.pprint(rj_stops['stops'][-1])
# Feeds not working
# pprint.pprint(rj_feeds)

# Acquire list of operators in area
operators_name = []
for op in rj_ops['operators']:
    operators_name.append([op['name'], op['metro']])
pprint.pprint(operators_name)

# Append number of stops and routes for each operator...coming soon

# Create list of stops, operators, and openID numbers
stop_list = []
for stop in rj_stops['stops']:
    stop_list.append([stop['name'], stop['onestop_id']])
pprint.pprint(stop_list)

