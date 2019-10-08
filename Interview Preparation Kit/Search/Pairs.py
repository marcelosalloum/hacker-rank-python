#!/bin/python3
# Problem Statement: https://www.hackerrank.com/challenges/pairs/problem

# Complete the pairs function below.
def pairs(k, arr):
    count_values = {}
    occurences = 0

    for key in range(len(arr)):
        value = arr[key]
        count_values[value] = count_values.get(value, 0) + 1

    for key in range(len(arr)):
        value = arr[key]
        if k == 0:
            occurences = count_values[value]
            break

        occurences += count_values.get(value + k, 0)
        
    return occurences

print(pairs(2, [1, 5, 3, 4, 2]))