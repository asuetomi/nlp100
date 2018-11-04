# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

counter = 0

with open('hightemp.txt') as f:
    for line in f:
        counter += 1

print(counter)
