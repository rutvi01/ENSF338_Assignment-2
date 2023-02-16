import sys
sys.setrecursionlimit(20000)
import json
import time
import matplotlib.pyplot as plt

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open('ex2.json', 'r') as f:
    input_data = json.load(f)

times = []

for ary in input_data:
    starting_time = time.time()
    func1(ary, 0, len(ary)-1)
    ending_time = time.time()
    times.append(ending_time - starting_time)

plt.plot(range(len(input_data)), times)
plt.xlabel('Input')
plt.ylabel('Time')
plt.title("Plot 2.2")
plt.show()