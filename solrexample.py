from urllib2 import Request, urlopen, URLError
import json

import time

start_time = time.time()

request = Request("http://54.173.242.173:8983/solr/comments/select?q=body:insane&rows=10000&wt=json")
response = urlopen(request)

player_json = json.loads(response.read())

print player_json['response']['docs'][9999]
elapsed_time = time.time() - start_time
print "elapsed time in seconds: " + str(elapsed_time)