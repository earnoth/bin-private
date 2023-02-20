#!/usr/bin/python

import simplejson
import urllib
import urllib2
import pprint
import postfile

report_url = "https://www.virustotal.com/vtapi/v2/file/report"
submit_url = "https://www.virustotal.com/vtapi/v2/file/scan"
parameters = {"resource": "c9dcdb2c57a3726ea31711242568a8d5",
	      "apikey": "53b71b10cb1c1f1d3c9a7eacdf32490acc17d5315805c3c2a8c47ec17dcfd272",
              "allinfo": "1"}

data = urllib.urlencode(parameters)
req = urllib2.Request(report_url, data)
response = urllib2.urlopen(req)
json = response.read()
data = simplejson.loads(json)
pprint.pprint(data)

