# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．


with open('col1.txt', encoding='UTF-8') as c1\
    , open('col2.txt', encoding='UTF-8') as c2\
    , open('col12.txt', 'w', encoding='UTF-8') as c12:
    for col1, col2 in zip(c1, c2):
        c12.write(col1.replace('\n', '\t') + col2)
