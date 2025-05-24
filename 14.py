number=input("カンマ区切りで整数を入力してください")
numbers = number.split(",")
numbers = [int(x) for x in numbers if x.strip() != ""]
length = len(numbers)
guusuu =  []
kisuu = []
for i in range(length):
    if numbers[i] % 2 == 0:
        guusuu.append(numbers[i])
    else:
        kisuu.append(numbers[i])
print("偶数は" + str(guusuu)+"奇数は"+str(kisuu))
