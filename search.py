#!/usr/bin/env python

import json
import urllib
import sys
import pprint

if len(sys.argv) != 3:
  print "[+] USAGE: python search.py <apikey> <domain>"
  sys.exit(1)

apikey = sys.argv[1]
domain = sys.argv[2]

url = "https://www.virustotal.com/vtapi/v2/domain/report"
parameters = {'domain':domain,'apikey':apikey}
response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
response_dict = json.loads(response)

pprint.pprint(response_dict)
