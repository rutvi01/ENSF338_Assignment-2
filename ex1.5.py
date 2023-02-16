import time
import matplotlib.pyplot as plt


def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)


def func_memo(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = func_memo(n-1, memo) + func_memo(n-2, memo)
    return memo[n]


a = range(36)
original = []
memoized = []

for i in a:
    starting_time = time.time()
    func(i)
    ending_time = time.time()
    original.append(ending_time - starting_time)
    
    starting_time = time.time()
    func_memo(i)
    ending_time = time.time()
    memoized.append(ending_time - starting_time)


plt.plot(a, original, label='Original')
plt.plot(a, memoized, label='Memoized')
plt.xlabel('Input n')
plt.ylabel('Time')
plt.title('Comparison of Functions')
plt.legend()
plt.show()
