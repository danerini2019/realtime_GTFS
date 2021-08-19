import pandas as pd
import os
import requests
import pprint
import time

header = {'apikey':os.environ.get('TRANSIT_LAND_API_KEY')}

# Geographic entries - test set
longitute = 37.816036
latitude = -122.230025
radius = 1000
after = 0

def api_call(lon, lat, r, after):
    query_url = 'https://transit.land/api/v2/rest/stops?after=' + str(after) + '&lon=' + str(longitute) + '&lat=' + str(latitude) + '&radius=' + str(r)
    resp_stops = requests.get(query_url, headers=header)
    stops_json = resp_stops.json()
    message = stops_json.get('message', None)
    stops_meta = stops_json.get('meta', None)
    if stops_meta:
        after = stops_meta['after']
    elif message:
        print(stops_json.keys())
        print(message)
        time.sleep(30)
        stops_json, stops_meta, after, message = api_call(lon, lat, r, after)
    
    return stops_json, stops_meta, after, message

def get_stops(lon, lat, r, after):
    page_count = 0
    stops_meta = {'meta': []}
    stops_all = {'stops': []}
    while stops_meta:
        stops_json, stops_meta, after, message = api_call(lon, lat, r, after)
        stops_all['stops'].extend(stops_json['stops'])
    return stops_all

stops_page_1 = get_stops(longitute, latitude, radius, after)
# pprint.pprint(stops_page_1['stops'])
print(len(stops_page_1['stops']))




# def count()
#     recursive count
#     num_count = how many times we need to query


# def get_page_afters(num_count):
#     []
#     for i in range(len(num_count)):
#         run query to get actual page after
#         add to list

#     return list of page afters 

# ----- vs ------

# def recursive_get_afters:
#     call query ? num of time 
#     return list of page afters







# Function to get next page number
def get_after(after):
    rj_stops_new = get_query_stops(after)
    return rj_stops_new.get('meta', None)

# def turn_page()


# purpose of API_GET.py
# Access transit.lane api
# pull stop data (and others) by page and accumulate jsons into list (will change)
# pull next page number from json and repeat previous step with next page
# catch when api limit is reached and wait for some amount of time before proceeding
# repeat until there is no more data
# store data in dataframe or something


# function for handle_limit, handle_page?? 


# while loop acquire stops json by the 20 and pull 
# after value each time. KeyError at after=1982. Why does
# does this happen?


# after = 0
# new_after = 1
# df_rj_stops = pd.DataFrame()

# while after != new_after:
#     after = new_after
#     rj_stops_new, new_after = query_stops(after)
#     df_rj_stops.append(rj_stops_new)
#     # pprint.pprint(rj_stops_new['stops'][-1])
#     print(new_after)

# print(df_rj_stops.head())


# Bay area rectangle select
# tl_query_age = 'https://transit.land/api/v2/rest/agencies?bbox=-122.503607,37.166611,-121.713958,38.038060'
# tl_query_ops = 'https://transit.land/api/v2/rest/operators?bbox=-122.503607,37.166611,-121.713958,38.038060'
# tl_query_routes = 'https://transit.land/api/v2/rest/routes?bbox=-122.503607,37.166611,-121.713958,38.038060'
# tl_query_stops = 'https://transit.land/api/v2/rest/stops?after=10000070&bbox=-122.503607,37.166611,-121.713958,38.038060?'
# tl_query_feeds = 'https://transit.land/api/v2/rest/feeds?bbox=-122.503607,37.166611,-121.713958,38.038060'

# # # Brooklyn example rectangle selectß
# # # tl_query = 'https://transit.land/api/v1/stops?bbox=-73.97339,40.649778,-73.946532,40.670353' 


# resp_age = requests.get(tl_query_age, headers=header)
# resp_ops = requests.get(tl_query_ops, headers=header)   
# resp_routes = requests.get(tl_query_routes, headers=header)
# resp_stops = requests.get(tl_query_stops, headers=header)
# resp_feeds = requests.get(tl_query_feeds, headers=header)

# rj_age = resp_age.json()
# rj_ops = resp_ops.json()
# rj_routes = resp_routes.json()
# rj_stops = resp_stops.json()
# rj_feeds = resp_feeds.json()

# read_age = pd.json_normalize(rj_age)
# read_ops = pd.json_normalize(rj_ops)
# read_routes = pd.json_normalize(rj_routes)
# read_stops = pd.json_normalize(rj_stops)
# read_feeds = pd.json_normalize(rj_feeds)

# df_age = pd.DataFrame(read_age)
# df_ops = pd.DataFrame(read_ops)
# df_routes = pd.DataFrame(read_routes)
# df_stops = pd.DataFrame(read_stops)
# df_feeds = pd.DataFrame(read_feeds)

# print(df_stops.head())
# pprint.pprint(len(rj_stops['stops']))
# pprint.pprint(rj_stops['meta'])