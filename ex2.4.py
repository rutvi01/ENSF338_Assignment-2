import sys
import json
import time
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    mid = (start + end) // 2
    array[mid], array[start] = array[start], array[mid]
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
    inputs_arrays = json.load(f)

    
times = []
for ary in inputs_arrays:
    starting_time = time.time()
    func1(ary, 0, len(ary)-1)
    end_timing = time.time()
    times.append(end_timing - starting_time)

plt.plot(range(len(inputs_arrays)), times)
plt.xlabel('Input')
plt.ylabel('Time')
plt.title("plot 2.4")
plt.show()