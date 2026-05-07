#フィボナッチ数列の関数を作る
#2～は=で出た数と足した2番目の数を足す　ということは-1,-2ってことになる

def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)
