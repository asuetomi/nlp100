# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

ret = ''

with open('hightemp.txt', encoding='utf-8') as f:
    for line in f:
        ret += line

print(ret.replace("\t", " "))
