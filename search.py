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

if response_dict["response_code"] == 1 and len(response_dict["detected_communicating_samples"]) >= 1:
  for hashes in response_dict["detected_communicating_samples"]:
    print "[+] %s:%s" % ( domain, hashes["sha256"] )
else:
  print "[-] %s: No samples found" % domain

#pprint.pprint(response_dict)

