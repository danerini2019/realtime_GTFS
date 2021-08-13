import pandas as pd
import os
import requests
import pprint
import time

header = {'apikey':os.environ['TRANSIT_LAND_API_KEY']}

# function to get a page of stops and next page number  
def get_query_stops(after):
    tl_query_stops = 'https://transit.land/api/v2/rest/stops?after=' + str(after) + '&bbox=-122.503607,37.166611,-121.713958,38.038060?'
    resp_stops = requests.get(tl_query_stops, headers=header)
    rj_stops_new = resp_stops.json()
    new_after_meta = rj_stops_new.get('meta', None)
    if new_after_meta:
        return rj_stops_new
    else:
        new_after = after
        time.sleep(5)

    return rj_stops_new

df_rj_stops = pd.DataFrame()
pprint.pprint(get_query_stops(1)['stops'][-1])
stops_page_1 = pd.DataFrame.from_dict(get_query_stops(1)['stops'])
print(stops_page_1.columns)
after_page_1 = stops_page_1['meta']['after']
print(after_page_1)
stops_page_2 = pd.DataFrame.from_dict(get_query_stops(after_page_1)['stops'])
pprint.pprint(stops_page_2.head())
df_rj_stops.append(stops_page_1)
df_rj_stops.append(stops_page_2)
print(df_rj_stops.head(100))


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