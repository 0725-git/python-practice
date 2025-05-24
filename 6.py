def check_age():
    print("関数を起動しました")
    age = int(input("年齢を入力してください："))

    if age < 18:
        print("未成年です")
    elif age < 65:
        print("成人です")
    else:
        print("高齢者です")

    print("あなたの年齢は" + str(age) + "歳です")

check_age()
