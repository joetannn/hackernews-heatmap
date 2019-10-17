
import requests
import json
from datetime import datetime


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

f = open(datetime.now().strftime("%m_%d_%Y") + ".json", 'w')
json = json.dumps(data_dump, indent=4, sort_keys=True)
f.write(json)
f.close()