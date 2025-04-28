score=input("点数をカンマ区切りで5つ入力してください")
score=score.split(",")
int_score = [int(x) for x in score if x.strip() != ""]
length=len(int_score)
for i in range(length):
    if int_score[i] >= 80:
        print(str(int_score[i])+"点で優秀")
    elif int_score[i] >= 60:
        print(str(int_score[i])+"点で合格")
    else:
        print(str(int_score[i])+"点で再試験")
