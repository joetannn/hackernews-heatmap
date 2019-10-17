
import requests
import json
from datetime import datetime
import re


data_dump = []

print("Starting requests...")
base_url = "https://hacker-news.firebaseio.com/v0/"
top_stories = "topstories"
best_stories = "beststories"
item = "/item/"
json_appender = ".json?print=pretty"

# get current top stories
print("Getting top stories...")
r = requests.get(url=base_url + top_stories + json_appender).json()

print("Acquiring info of top 100 stories...")
for i in range(100):
    data_dump.append(requests.get(url=base_url + item + str(r[i]) + json_appender).json())
    pass

# dump the data as json
f = open(datetime.now().strftime("%m_%d_%Y") + ".json", 'w')
json = json.dumps(data_dump, indent=4, sort_keys=True)
f.write(json)
f.close()

# get titles
title_data = []
for j in data_dump:
    title_data.append(j.get('title'))


# create word frequency list
frequency_dict = {}
split_title = []
for k in title_data:
    split_title = k.split(" ")
    print(split_title)
    for m in split_title:
        m = re.sub("[^a-zA-Z]+", "", m).lower()
        if m in frequency_dict.keys():
            frequency_dict[m] = (frequency_dict.get(m)) + 1
        else:
            frequency_dict[m] = 1

print(frequency_dict)

# TODO: create ignored word list
# TODO: add point values