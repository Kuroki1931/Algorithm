"""
((n & (n-1)) == 0)について説明する。

例
奇数　-> 1のくらいが0になるだけ。
5  101  100       100
11 1011 1010      1010

6  110   101       100
8  1000  111       0
"""

# 答え
# nが2^xで表現できるかどうか。
