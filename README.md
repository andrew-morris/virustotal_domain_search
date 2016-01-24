# virustotal_domain_search
Search a domain on VirusTotal to identify if any known malware samples have ever attempted to communicate with it

# Usage

```
$ python search.py blahblahasdkjsdjfhskdjfhksdkadshfkahjdsf 027.ru

{u'BitDefender category': u'parked',
 u'Websense ThreatSeeker category': u'uncategorized',
 u'Webutation domain info': {u'Adult content': u'yes',
                             u'Safety score': 40,
                             u'Verdict': u'malicious'},
 u'categories': [u'parked', u'uncategorized'],
 u'detected_downloaded_samples': [{u'date': u'2013-06-20 18:51:30',
                                   u'positives': 2,
                                   u'sha256': u'cd8553d9b24574467f381d13c7e0e1eb1e58d677b9484bd05b9c690377813e54',
                                   u'total': 46}],
 u'detected_urls': [{u'positives': 1,
                     u'scan_date': u'2016-01-18 08:48:40',
                     u'total': 66,
                     u'url': u'http://027.ru/'},
                    {u'positives': 2,
                     u'scan_date': u'2015-02-18 08:54:52',
                     u'total': 62,
                     u'url': u'http://027.ru/index.html'}],
 u'domain_siblings': [],
 u'resolutions': [{u'ip_address': u'62.210.11.121',
                   u'last_resolved': u'2016-01-18 00:00:00'},
                  {u'ip_address': u'90.156.201.11',
                   u'last_resolved': u'2013-05-03 00:00:00'},
                  {u'ip_address': u'90.156.201.14',
                   u'last_resolved': u'2013-05-07 00:00:00'},
                  {u'ip_address': u'90.156.201.27',
                   u'last_resolved': u'2013-04-01 00:00:00'},
                  {u'ip_address': u'90.156.201.71',
                   u'last_resolved': u'2013-05-01 00:00:00'},
                  {u'ip_address': u'90.156.201.97',
                   u'last_resolved': u'2013-06-20 00:00:00'}],
 u'response_code': 1,
 u'subdomains': [u'www.027.ru'],
 u'undetected_referrer_samples': [{u'positives': 0,
                                   u'sha256': u'b8f5db667431d02291eeec61cf9f0c3d7af00798d0c2d676fde0efb0cedb7741',
                                   u'total': 53}],
 u'verbose_msg': u'Domain found in dataset',
 u'whois': u'domain:        027.RU\nnserver:       ns1.masterhost.ru.\nnserver:       ns2.masterhost.ru.\nnserver:       ns.masterhost.ru.\nstate:         REGISTERED, DELEGATED, VERIFIED\nperson:        Private Person\nregistrar:     RU-CENTER-RU\nadmin-contact: https://www.nic.ru/whois\ncreated:       2005.12.09\npaid-till:     2016.12.09\nfree-date:     2017.01.09\nsource:        TCI',
 u'whois_timestamp': 1453101595.63224}
```
