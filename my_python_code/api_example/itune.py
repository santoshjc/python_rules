""" APIs is used to request something from the web , for that i have
installed `requests` package using `pip install requests` command"""

""" JSON is standard txt format, Json is typically used now a days as a
language agnostic format for exchanging data between computers"""

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent=2)) #nice formating of JSON file

o = response.json()
for result in o["results"]:
    print(result["trackName"])

""" to use this API , Write `python itunes.py [singer name]` in terminal """
