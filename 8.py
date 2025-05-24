# 関数の定義
"""
def judge_age(age):
    if age < 18:
        return "未成年"
    elif age < 65:
        return "成人"
    else:
        return "高齢者"

# メイン処理（関数を使う部分）
for i in range(3):
    age = int(input("年齢を入力してください："))
    name = input("名前を入力してください：")
    result = judge_age(age)
    print(str(i+1) + "人目は" + name + "さんで年齢は" + result + "です")
"""
def judge_seibetu(seibetu):
    if seibetu == "男":
        return "男性"
    elif seibetu == "女":
        return "女性"
    else:
        return "不明"
# メイン処理（関数を使う部分）
for i in range(3):
    age = int(input("年齢を入力してください："))
    name = input(" 名前を入力してください：")
    seibetu = input("性別を入力してください（男/女）：")
    result = judge_age(age)
    result2 = judge_seibetu(seibetu)
    print(str(i+1) + "人目は" + name + "さんで年齢は" + result + "で性別は" + result2 + "です")