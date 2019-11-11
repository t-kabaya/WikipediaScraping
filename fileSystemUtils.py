def createCacheForTest(json):
  f = open("mockResponse.json", "w+")

  # f.writeの引数は、stirngでないとダメだった。
  f.write(str(json))
  f.close