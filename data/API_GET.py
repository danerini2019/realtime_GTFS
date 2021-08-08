import os
import requests

# Bay area rectangle select
tl_query_age = 'https://transit.land/api/v2/rest/agencies?bbox=-122.503607,37.166611,-121.713958,38.038060'
tl_query_ops = 'https://transit.land/api/v2/rest/operators?bbox=-122.503607,37.166611,-121.713958,38.038060'
tl_query_routes = 'https://transit.land/api/v2/rest/routes?bbox=-122.503607,37.166611,-121.713958,38.038060'
tl_query_stops = 'https://transit.land/api/v2/rest/stops?bbox=-122.503607,37.166611,-121.713958,38.038060'
tl_query_feeds = 'https://transit.land/api/v2/rest/feeds?bbox=-122.503607,37.166611,-121.713958,38.038060'

# # Brooklyn example rectangle selectß
# # tl_query = 'https://transit.land/api/v1/stops?bbox=-73.97339,40.649778,-73.946532,40.670353' 

header = {'apikey':os.environ['TRANSIT_LAND_API_KEY']}

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
