import pandas as pd
import os
import requests
import pprint

header = {'apikey':os.environ['TRANSIT_LAND_API_KEY']}

def query_stops(after):
    tl_query_stops = 'https://transit.land/api/v2/rest/stops?after=' + str(after) + '&bbox=-122.503607,37.166611,-121.713958,38.038060?'
    resp_stops = requests.get(tl_query_stops, headers=header)
    rj_stops = resp_stops.json()
    new_after = rj_stops['meta']['after']
    return rj_stops, new_after

# for loop acquire stops json by the 20 and pull 
# after value each time. KeyError at after=1982. Why does
# does this happen?
after = 0
new_after = 1
rj_stops = []

while after != new_after:
    after = new_after
    rj_stops_new, new_after = query_stops(after)
    rj_stops.append(rj_stops_new)
    print(len(rj_stops))
    print(new_after)


# Bay area rectangle select
tl_query_age = 'https://transit.land/api/v2/rest/agencies?bbox=-122.503607,37.166611,-121.713958,38.038060'
tl_query_ops = 'https://transit.land/api/v2/rest/operators?bbox=-122.503607,37.166611,-121.713958,38.038060'
tl_query_routes = 'https://transit.land/api/v2/rest/routes?bbox=-122.503607,37.166611,-121.713958,38.038060'
tl_query_stops = 'https://transit.land/api/v2/rest/stops?after=10000070&bbox=-122.503607,37.166611,-121.713958,38.038060?'
tl_query_feeds = 'https://transit.land/api/v2/rest/feeds?bbox=-122.503607,37.166611,-121.713958,38.038060'

# # Brooklyn example rectangle selectß
# # tl_query = 'https://transit.land/api/v1/stops?bbox=-73.97339,40.649778,-73.946532,40.670353' 


resp_age = requests.get(tl_query_age, headers=header)
resp_ops = requests.get(tl_query_ops, headers=header)   
resp_routes = requests.get(tl_query_routes, headers=header)
resp_stops = requests.get(tl_query_stops, headers=header)
resp_feeds = requests.get(tl_query_feeds, headers=header)

rj_age = resp_age.json()
rj_ops = resp_ops.json()
rj_routes = resp_routes.json()
rj_stops = resp_stops.json()
rj_feeds = resp_feeds.json()

read_age = pd.json_normalize(rj_age)
read_ops = pd.json_normalize(rj_ops)
read_routes = pd.json_normalize(rj_routes)
read_stops = pd.json_normalize(rj_stops['stops'])
read_feeds = pd.json_normalize(rj_feeds)

df_age = pd.DataFrame(read_age)
df_ops = pd.DataFrame(read_ops)
df_routes = pd.DataFrame(read_routes)
df_stops = pd.DataFrame(read_stops)
df_feeds = pd.DataFrame(read_feeds)

# print(df_stops.head())
pprint.pprint(len(rj_stops['stops']))
pprint.pprint(rj_stops['meta'])