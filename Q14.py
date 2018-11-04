#! python3
# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
#from  __future__ import print_function

import sys
print(sys.version)


argv = sys.argv
argc = len(argv)
if argc != 3:
    print('usage:' + argv[0]+ ' N filename')
    quit()

#print(argv)
i = 0
N = int(argv[1])
#print('N={}'.format( N))

with open('hightemp.txt', encoding='utf-8') as f:
    # with open('hightemp.txt',encoding='utf-8') as f:
    # with open(argv[2], encoding='utf-8') as f:
    # print('open!')
    for line in f:
        #print(line)
        #print('i={}, N={}'.format(i, N))
        if (i < N):
            #print('i={} < N={}'.format(i, N))
            print(line, end='')
            i += 1
        else:
            #print('i={} >= N={}'.format(i, N))
            quit()

