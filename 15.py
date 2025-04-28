number = input("カンマ区切りで整数を入力してください")
numbers = number.split(",")
numbers = [int(x) for x in numbers if x.strip() != ""]
length = len(numbers)
guusuu = []
kisuu = []
for x in range(length):
    if numbers[x] % 2 == 0:
        guusuu.append(2*numbers[x])
    else:
        kisuu.append(3*numbers[x])
print("入力された偶数を2倍したものは" + str(guusuu) + "3倍した奇数は" + str(kisuu))