# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

import re

ret = ''

with open('hightemp.txt', encoding='utf-8') as f:
    for line in f:
        # re.sub(r"\t", " ", line, -1)
        # line.replace("\t", " ")
        ret += line

print(ret.replace("\t", " "))
