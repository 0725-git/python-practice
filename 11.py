'''
from numpy import average
input_str=input("数字をカンマで入力して下さい")
scores=input_str.split(",")
scores = [int(x) for x in scores if x.strip() != ""]
len=4
print("合計"+ str(sum(scores)))
print("平均"+ str(average(scores)))
print("最大値"+ str(max(scores)))
print("最小値"+ str(min(scores)))
'''
'''
inputfoods=input("あなたの好きな食べ物をカンマで3つ入力してください")
foods=inputfoods.split(",")
len=3
print("あなたの好きな食べ物は"+ str(foods[0]) + "、" + str(foods[1]) + "、" + str(foods[2]) + "です")
'''
'''
inputnumbers=input("好きな数字をカンマで3つ入力してください")
inputnumbers=inputnumbers.split(",")
len=3
inputnumbers = [int(x) for x in inputnumbers if x.strip() != ""]
print("合計"+str(sum(inputnumbers)))
print("平均"+str(average(inputnumbers)))
'''
'''

'''
