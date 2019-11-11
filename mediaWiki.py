import requests 
from fileSystemUtils import createCacheForTest
 
title = '世界の果てまでイッテQ!'

# api-endpoint 
URL = 'https://ja.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=xmlfm&titles=' + title + '&rvsection=0&format=json'

response = requests.get(url = URL).json()

# 341000が何を意図する  
infoBox = response['query']['pages']['341000']
print(infoBox)

createCacheForTest(infoBox)