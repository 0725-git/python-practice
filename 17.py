'''
data = input("名前と得点をカンマ区切りで入力してください")
data = data.split(",")
data = [x.strip() for x in data if x.strip() != ""]
scores = {}
length = len(data)

for i in range(0, len(data), 2):
    names = data[i]
    points = int(data[i + 1])

    scores[names] = points
    
for names, scores in scores.items():
    if scores >= 80:
        print(names + " さんは合格です")
    else:
        print(names + " さんは不合格です")
'''
data = input("名前と得点をカンマ区切りで入力してください")
data = data.split(",")
data = [x.strip() for x in data if x.strip() != ""]
scores = {}
length = len(data)

for i in range(0, len(data), 2):
    names = data[i]
    points = int(data[i + 1])

    scores[names] = points
    
print(scores)