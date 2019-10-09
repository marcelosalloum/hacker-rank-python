#!/bin/python3
# Problem Statement: Ref: https://www.hackerrank.com/challenges/minimum-time-required/problem

import math

def minTime(machines, goal):
    low = int(1)
    high = int(10e18)
    result = high

    while low <= high:
        done = 0
        mid = int((high + low) / 2)
        for machine_capacity in machines:
            done += int(mid / machine_capacity)

        if done >= goal:
            high = mid - 1
            result = mid
        else:
            low = mid + 1

    return result

print(minTime([4, 5, 6], 12))