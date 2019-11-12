import json

def parseMockResponseFromFile():
  f = open("mockResponse.json", "r")

  # stringから、jsonへの、変換には、dumpsと、loadsという関数が必要。
  mockResponse = json.loads(json.dumps(f.read()))
  # print(is_json(mockResponse))

  return mockResponse


def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True