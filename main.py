import wikipedia
wikipedia.set_lang("ja")

def createSummary(title):
  contentArray = wikipedia.page(title).content.splitlines()
  
  print(wikipedia.page(title).summary)
  talentList = []
  # フラグ
  isTalentLine = False
  for line in contentArray:
    if '=== 出演者 ===' in line:
      isTalentLine = True
    elif '=== レギュラー ===' in line:
      isTalentLine = True
    elif '=== 準レギュラー ===' in line:
      isTalentLine = True
    elif line == '':
      isTalentLine = False

    if isTalentLine == True:
      talentList.append(line)

  print(talentList)


  # content
  # print(contentArray)

# 水曜日のダウンタウンは成功

createSummary('世界の果てまでイッテQ!')