def get_scores():
    data = input("カンマ区切りで名前と点数を入力してください ")
    data = data.split(",")
    data = [x.strip() for x in data if x.strip() != ""]
    scores = {}
    length = len(data)
    for i in range(0, len(data), 2):
        name = data[i]
        score = int(data[i + 1])
        scores[name] = score
    return scores

def print_success(scores):
    for name, score in scores.items():
        if score >= 60:
            print(f"{name}さんは合格です。")
    return True
def print_failure(scores):
    for name, score in scores.items():
        if score < 60:
            print(f"{name}さんは不合格です。")
    return True

def main():
    scores = get_scores()
    print_success(scores)
    print_failure(scores)
if __name__ == "__main__":
    main()