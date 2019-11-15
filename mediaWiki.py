import requests 
import re 

# title = '世界の果てまでイッテQ!'
# title = '徹子の部屋'
# title = '同期のサクラ'
# title = '水曜日のダウンタウン'
# title = '今夜くらべてみました'
# title = '歴史秘話ヒストリア'
title = 'ホンマでっか!?TV' # ['明石家さんま', '加藤綾子', 'フリーアナウンサー', 'ブラックマヨネーズ', '小杉竜一', '吉田敬', '磯野貴理子', '島崎和歌子']

# api-endpoint 
URL = 'https://ja.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=xmlfm&titles=' + title + '&rvsection=0&format=json'

response = requests.get(url = URL).json()['query']['pages']

# 341000などの数字は何を意図する?
# jsonの最初のkeyのvalueを取得
rawTalentData = response[list(response.keys())[0]]['revisions'][0]['*'].splitlines()
# print(rawTalentData)

talentString = ''
for line in rawTalentData:
  if '出演者' in line:
    talentString = line
    break


talentList = re.findall(r"\[(\w+)\]", talentString)
print(talentList)
