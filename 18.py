#importはモジュールをインポートするためのキーワード
#numpyは数値計算ライブラリ
#averageは平均値を計算する関数
from numpy import average
data = input("名前と得点をカンマ区切りで入力してください")
data = data.split(",")
#stripは文字列の前後の空白を削除するメソッド
data = [x.strip() for x in data if x.strip() != ""]
scores = {}
length = len(data)
for i in range(0, len(data), 2):
    names = data[i]
    points = int(data[i + 1])
#.values()は辞書の値を取得するメソッド
    average_score = sum(scores.values()) / (length / 2)
#scores[names] = pointsでscores辞書に名前と点数を対になるよう追加
    scores[names] = points
print("最高点数は" + str(max(scores.values()))+"で" + str(max(scores, key=scores.get)) + "さんです")
for i in range(0, len(data), 2):
    names = data[i]
    points = int(data[i + 1])

pass_list=[]
#.items()は辞書のキーと値のペアを取得するメソッド
for name, score in scores.items():
    if score >= 80:
#appendはリストの末尾に要素を追加するメソッド
        pass_list.append(name)
#合格者の名前を表示
print("合格者は" + str(pass_list) + "さん")