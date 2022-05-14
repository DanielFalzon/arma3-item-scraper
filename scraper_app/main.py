import urllib.request
import ssl
import lxml.html

from pprint import pprint

try:
    ssl._create_default_https_context = ssl._create_unverified_context
    req = urllib.request.Request(url="https://community.bistudio.com/wiki/Arma_3:_CfgVehicles_WEST")

    with urllib.request.urlopen(req) as inpt:
        html_doc = lxml.html.fromstring(inpt.read())
        print(html_doc)

except urllib.error.URLError as e:
    print(e.reason)