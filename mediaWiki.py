import requests 
import re
from fileSystemUtils import createCacheForTest
 
title = '世界の果てまでイッテQ!'

# api-endpoint 
URL = 'https://ja.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=xmlfm&titles=' + title + '&rvsection=0&format=json'

response = requests.get(url = URL).json()

# 341000が何を意図する?
infoBox = response['query']['pages']['341000']['revisions'][0]['*']

infoBoxArray = infoBox.splitlines()
# print(infoBox)
# print(infoBoxArray)

talentList = ''
# フラグ
isTalentLine = False
for line in infoBoxArray:
  if '|出演者=' in line:
    isTalentLine = True
  elif '|' in line:
    isTalentLine = False

  if isTalentLine == True:
    talentList = line

# print(talentList)

# 制作途中
prettifiedTalentList = re.findall(r"[^[]*\[([^]]*)\]", talentList)

print(prettifiedTalentList)

# extractedTalentList