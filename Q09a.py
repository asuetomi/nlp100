# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random

def word_Typoglycemia(word):
    if (len(word) <= 4):
        return word
    else:
        split_list = list(word[1:-1])
        random.shuffle(split_list)
        return word[0] + "".join(split_list) + word[-1]

def str_Typoglycemia(str):
    words = str.split(" ")
    ret = []
    for word in words:
        word = word_Typoglycemia(word)
        ret.append(word)
    return " ".join(ret)

str = "I couldn't believe that I could actually understand \
what I was reading : the phenomenal power of the human mind ."

print(str_Typoglycemia(str))