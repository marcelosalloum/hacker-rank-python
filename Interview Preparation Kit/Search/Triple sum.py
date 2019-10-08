#!/bin/python3
# Problem Statement: https://www.hackerrank.com/challenges/triple-sum/problem

# Complete the pairs function below.
def triplets(a, b, c):
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))
    
    [b_key, a_key, c_key] = [0, 0, 0]
    result = 0
    
    while b_key < len(b):
        while a_key < len(a) and a[a_key] <= b[b_key]:
            a_key += 1
        
        while c_key < len(c) and c[c_key] <= b[b_key]:
            c_key += 1

        result += a_key * c_key
        b_key += 1

    return result

print(triplets([1, 1, 1, 1, 3, 5], [2, 3], [1, 1, 1, 1, 2, 3]))