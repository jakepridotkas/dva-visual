# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:30:45 2018

@author: prido
"""

import pandas as pd
import requests
import time
import json

API_KEY = "DONT PUSH"

results = []
response_passes = []
append_passes = []

#number of rows
rng = 100
start_time = time.time()

colnames = ['ID', 'STREET_NUM', 'PREFIX', 'STREET', 'SUFFIX', 'ZIP']

PROP = pd.read_csv('results.csv', names = colnames, nrows=rng, dtype = str)
#print(PROP[1:5])
PROP['PREFIX'].fillna('', inplace=True)
PROP['STREET_NUM'].fillna('0', inplace=True)


for i in range(rng):      
    try:
        response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + \
                                PROP['STREET_NUM'][i] + "+" \
                                + PROP['PREFIX'][i] + "+" \
                                + PROP['STREET'][i] + "+" \
                                + PROP['SUFFIX'][i] + "+" \
                                + PROP['ZIP'][i] + "+" \
                                "&key=" + API_KEY)
    except:
        #response_passes.append(i)
        pass
        
    data = response.json()
    try:
        results.append([PROP['ID'][i],\
                        data['results'][0].get("formatted_address"),\
                        data['results'][0].get("geometry").get("location").get("lat"),\
                        data['results'][0].get("geometry").get("location").get("lng")])    
    except:
        #append_passes.append(i)
        pass
         
        
 #50 requests per second max, don't think I'll hit
print(str(rng) + " results in --- %s seconds ---" % (time.time() - start_time))
print("Writing to results file...")

#the file we write results to in the directory
f = open("results_lat_lng.csv", "w+")
f.write("ID,Address,City,State,Country,Lat,Long\n")
for x in results:
    f.write(str(x[0]) + ',' + str(x[1]) + ',' + str(x[2]) + ',' + str(x[3]) + "\n")
f.close()


