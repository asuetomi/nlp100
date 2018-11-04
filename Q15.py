# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

import sys

argv = sys.argv
argc = len(argv)

if (argc != 3):
    print('usage: {} N filename'.format( argv[0]))
    quit()

N = int(argv[1])
i = 0
buf = []

with open(argv[2], encoding='UTF-8') as f:
    for line in f:
        if (i < N):
            buf.append(line)
        else:
            buf[i % N] = line
        i += 1

# print(i)
for j in range(i - N, i):
    # print(j)
    print(j + 1, buf[j % N], end='')
