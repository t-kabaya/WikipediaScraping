
# 開発の効率化のため、一々APIアクセスをする代わりに、localにstaticなファイルとして保存しておく。
def createCacheForTest(json):
  f = open("mockResponse.json", "w+")

  # f.writeの引数は、stirngでないとダメだった。
  f.write(str(json))
  f.close