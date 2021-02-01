# 重複のない文字列か確認
# str -> bool

def check1(str):
    for i in range(len(str)):
        a = str[i]
        res = str[i+1:]
        for j in range(len(res)):
            if a == res[j]:
                return False
    return True

print(check1('apple') == False)
print(check1('Amazon') == True)

# 計算量はO(N^2)







"""
以下解答参照後
"""


# 文字コードがASCIIなのかUnicodeなのかの確認

# ①ASCII前提とした解き方。
def check2(str):
    if len(str) > 128:
        return False

    
    List = [False] * 128
    for i in range(len(str)):
        code_number = ord(str[i])
        if List[code_number] == True:
            return False
        else:
            List[code_number] = True

    return True

print(check2('apple') == False)
print(check2('Amazon') == True)

# 計算量はO(n), 消費メモリはO(1)





# ②ビット操作による解答
# chapter5でやります。

#######################################################


        

    





