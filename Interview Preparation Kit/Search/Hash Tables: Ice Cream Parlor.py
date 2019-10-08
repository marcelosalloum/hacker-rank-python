#!/bin/python3
# Problem Statement: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    array_size = len(cost)
    count_costs = {}

    k1 = -1
    k2 = -1
    v1 = -1
    v2 = -1

    for index in range(array_size):
        value = cost[index]
        count_costs[value] = count_costs.get(value, 0) + 1

    for k1 in range(array_size):
        if cost[k1] >= money:
            continue
        
        v1 = cost[k1]
        v2 = money - v1
        if v2 >= money:
            continue

        if v2 in count_costs.keys():
            if v2 != v1:
                break
            elif count_costs[v1] > 1:
                break
        
    printable_keys = []
    for key in range(array_size):
        value = cost[key]
        if value == v1 or value == v2:
            printable_keys.append(key + 1)
            if len(printable_keys) == 2:
                print(printable_keys[0], printable_keys[1])
                return

    


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
