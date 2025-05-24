import random
for i in range(5):
    age = random.randint(1, 100)
    if age < 18:
        print("未成年です")
    elif 18 <= age < 65:
        print("成人です")
    else:
        print("高齢者です")
    print(str(i+1)+"回目：年齢は" + str(age) + "歳です")