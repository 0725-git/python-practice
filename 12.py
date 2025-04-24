inputnumber=input("カンマ区切りで得点を5つ入力してください")
inputnumber=inputnumber.split(",")
length=5
print("平均"+str(len(inputnumber)))
inputnumber = [int(x) for x in inputnumber if x.strip() != ""]
for i in range (0, length):
    if inputnumber[i] >= 80:
        print(str(i+1)+"人目の点数は"+str(inputnumber[i])+"点で合格")
    else:
        print(str(i+1)+"人目の点数は"+str(inputnumber[i])+"点で不合格で平均との差は"+str(inputnumber[i]-len(inputnumber))+"点")
