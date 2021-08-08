import os
import requests
import tempfile
import sys
sys.path.insert(0, '../data/')
import API_GET

# import geopandas as gpd
import networkx as nx
# import osmnx as ox
import numpy as np
import pandas as pd
# import peartree as pt
# from shapely.geometry import Point
import pprint



pprint.pprint(rj_age['agencies'][0])
# pprint.pprint(rj_ops['operators'][0])
# pprint.pprint(rj_routes['routes'][0])
# pprint.pprint(len(rj_stops['stops'][0]))
# pprint.pprint(rj_feeds['feeds'][0])

# Acquire list of operators in area
# operators_name = []
# for op in rj_ops['operators']:
#     operators_name.append([op['name'], op['metro']])
# pprint.pprint(operators_name)

# Append number of stops and routes for each operator...coming soon

# Create list of stops, operators, and openID numbers
# stop_list = []
# for stop in rj_stops['stops']:
#     stop_list.append([stop['name'], stop['onestop_id']])
# # pprint.pprint(stop_list)
# print(stop_list)


