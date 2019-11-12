import requests 
import re 

# title = '世界の果てまでイッテQ!'
title = '徹子の部屋'

# api-endpoint 
URL = 'https://ja.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=xmlfm&titles=' + title + '&rvsection=0&format=json'

response = requests.get(url = URL).json()['query']['pages']

# 341000などの数字は何を意図する?
# jsonの最初のkeyのvalueを取得
rawTalentData = response[list(response.keys())[0]]['revisions'][0]['*'].splitlines()

talentList = ''
isTalentLine = False
for line in rawTalentData:
  if '|出演者=' in line:
    isTalentLine = True
  elif '|' in line:
    isTalentLine = False

  if isTalentLine == True:
    talentList = line

# 枝葉を取り除く
decentTalentList = re.findall(r"\[(\w+)\]", talentList)
print(decentTalentList)
