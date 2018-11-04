# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

with open('hightemp.txt', encoding='utf-8') as f\
        , open('col1.txt', 'w', encoding='utf-8') as c1 \
        , open('col2.txt', 'w', encoding='utf-8') as c2:
    for line in f:
        cols = line.split('\t')
        print(cols[0], file=c1)
        print(cols[1], file=c2)
