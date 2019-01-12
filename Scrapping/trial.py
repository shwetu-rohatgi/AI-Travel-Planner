import urllib.request
from bs4 import BeautifulSoup as bs
import json
# -*- coding: utf-8 -*-
# -*- coding: iso-8859-1 -*-
cities = ["Los Angeles", "Munich", "New York", "Mumbai", "Paris", "London"]
cities_url = ["https://www.lonelyplanet.com/usa/los-angeles",
              "https://www.lonelyplanet.com/germany/munich",
              "https://www.lonelyplanet.com/usa/new-york-city",
              "https://www.lonelyplanet.com/india/mumbai-bombay",
              "https://www.lonelyplanet.com/france/paris",
              "https://www.lonelyplanet.com/england/london"]
for url in cities_url:
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    f = urllib.request.urlopen(req)
    soup = bs(f, 'html.parser')
    script_text = soup.find(id="initialStateSights")
    text = script_text.get_text()

    d = json.loads(text)
    print("\nLocations in "+cities[cities_url.index(url)]+":")
    x = d["first_column"]
    for a in x:
        print(a["title"])
    x = d["second_column"]
    for a in x:
        print(a["title"])