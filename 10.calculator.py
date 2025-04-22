def calculator():
    print("電卓を起動しました")
while True:
    num1 = float(input("1つ目の数を入力してください："))
    op = input("演算子を入力してください（+ - * /）：")
    num2 = float(input("2つ目の数を入力してください："))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("0では割れません")
            continue
    else:
        print("演算子が無効です")
        continue

    print("あなたの入力の計算結果は：" + str(result) + " です")
    print("計算を続ける場合は、'y'を入力してください。終了する場合は、'n'を入力してください。")
    continue_calculation = input("続けますか？ (y/n): ")
    if continue_calculation.lower() != 'y':
        print("電卓を終了します")
        break

calculator()
