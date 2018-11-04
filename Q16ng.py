# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys

argv = sys.argv
argc = len(argv)

if (argc != 3):
    print('usage: Q16.py N filename')
    quit()

print(argv)
N = int(argv[1])
with open(argv[2], encoding = 'utf-8') as infile:
    f = [0] * N

    print(f)
    print(range(N))
    for i in range(N):
        f[i] = open('out{}'.format(i), 'w', encoding = 'utf-8')
    
    counter = 0    
    for line in infile:
        f[counter % N].write(line)
        counter += 1

    for i in range(N):
        f[i].close()

