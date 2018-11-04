# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def ngram(str, n):
    list = []
    for i in range(len(str)-n + 1):
        list.append(str[i:i+n])
    return list

if __name__ == '__main__':

    orgstr = "I am an NLPer"


    instr = orgstr.replace(' ', '')

    rlist2 =ngram(instr, 2)
    print(rlist2)
    rlist3 =ngram(instr, 3)
    print(rlist3)
    rlist4 =ngram(instr, 4)
    print(rlist4)

    words = orgstr.split()

    print(ngram(words, 2))