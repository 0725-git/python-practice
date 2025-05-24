"""
age = 20

if age >= 18:
    print("成人です")
else:
    print("未成年です")

age=33
if age <18:
    print("未成年です")
elif 18<=age<65:
    print("成人です")
else:
    print("高齢者です")
    
"""
import random
age=random.randint(1, 100)
if age < 18:
    print("未成年です")
elif 18 <= age < 65:
    print("成人です")
else:
    print("高齢者です")
print("あなたの年齢は"+str(age)+"歳です")