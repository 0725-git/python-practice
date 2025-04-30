'''
name = input("名前と点数をカンマ区切りで入力してください")
name = name.split(",")
name = [x.strip() for x in name if x.strip() != ""]
length = len(name)
for i in range(0, len(name), 2):
    names = name[i]
    points = int(name[i + 1])
    if points >= 80:
        print(names + "さんは"+str(points)+"点で合格です")
    else:
        print(names + "さんは"+str(points)+"点で不合格です")
'''

age = input("カンマ区切りで名前と年齢を入力してください")
age = age.split(",")
age = [x.strip() for x in age if x.strip() != ""]
length = len(age)
for i in range(0, len(age), 2):
    names = age[i]
    ages = int(age[i + 1])
    if ages < 18:
        print(names + "さんは未成年です")
    elif ages < 65:
        print(names + "さんは成人です")
    else:
        print(names + "さんは高齢者です")
