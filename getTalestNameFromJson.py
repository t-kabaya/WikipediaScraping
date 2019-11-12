from parseMockResponseFromFile import parseMockResponseFromFile
import json

# 開発用
apiResponse = json.load(json.dumps(parseMockResponseFromFile()))
print(apiResponse)

# 341000が何を意図する  
infoBox = apiResponse['query']['pages']['341000']
print(infoBox)