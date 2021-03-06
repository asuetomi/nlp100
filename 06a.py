# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

from Q05 import ngram

str1 = "paraparaparadise"
str2 = "paragraph"


print(str1)
print(str2)

X = set(ngram(str1, 2))
Y = set(ngram(str2, 2))

print('X =', X)
print('Y =', Y)

XandY = X.intersection(Y)
print('X & Y =', XandY)

XorY = X.union(Y)
print('X | Y =', XorY)

XsubY = X.difference(Y)
print('X - Y =', XsubY)

if 'se' in X:
    print('"se" in X', X)

if 'se' in Y:
    print('"se" in Y', Y)
