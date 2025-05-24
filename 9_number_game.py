import random
answer = random.randint(1, 100)
while True:
    count += 1
    suuji = int(input("数字を入力してください："))
    if suuji < 1 or suuji > 100:
        print("1~100の数字を入力してください")
        continue
    if suuji == answer:
        print("正解です"+str(count) + "回目で当たりました")
    elif suuji < answer:
        print("もっと大きい数字です")
    else:
        print("もっと小さい数字です")
    break