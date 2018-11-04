# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys

argv = sys.argv
argc = len(argv)

if argc != 3:
    print('usage: Q16.py N filename')
    quit()

# print(argv)
N = int(argv[1])

with open(argv[2], encoding='utf-8') as fin:
    lines = fin.readlines()

finlen = len(lines)
print('finlen = ', finlen)
foutlen = (finlen // N) + (1 if (finlen / N) != (finlen // N) else 0)

print('foutlen = ', foutlen)

counter = 0
for i in range(N):
    with open('out{}.dat'.format(i), 'w', encoding='utf-8') as fout:
        assert isinstance(i, object)
        for j in range(foutlen * i, (foutlen * (i + 1)) if i != (N - 1) else finlen):
            fout.write(lines[counter])
            counter += 1
