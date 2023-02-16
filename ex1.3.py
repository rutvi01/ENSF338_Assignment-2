def func_memo(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0 or n == 1:
        return n
    else:
        output = func_memo(n-1, memo) + func_memo(n-2, memo)
        memo[n] = output
        return output
print(func_memo(30))
