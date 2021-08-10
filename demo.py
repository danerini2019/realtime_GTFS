import os
import requests
import tempfile
import sys
from data.API_GET import rj_age, rj_ops, rj_routes, rj_stops, rj_feeds
from data.API_GET import resp_age, resp_ops, resp_routes, resp_stops, resp_feeds

import networkx as nx
import numpy as np
import pandas as pd
import pprint

# pprint.pprint(rj_feeds['feeds'][-5])
# pprint.pprint(len(rj_feeds['feeds']))
# pprint.pprint(rj_ops['operators'][0])
# pprint.pprint(rj_routes['routes'][0])
# nt.pprint(len(rj_stops['stops'][0]))
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

# Create list of feeds and their urls, etc.
# feed_list = []
# for feed in rj_feeds['feeds']:
#     feed_list.append([feed['onestop_id']])
# pprint.pprint(feed_list)

# pprint.pprint(rj_feeds['feeds'][3])

 


