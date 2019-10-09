def maximumSum(a, m):

    result = 0
    prefix_sum = {0: a[0]}

    index = 1
    while index < len(a):
        prefix_sum[index] = prefix_sum[index - 1] + a[index]
        index += 1

    for end in range(len(a)):
        for start in range(end + 1):
            if start == end:
                diff = a[start]
            elif start == 0:
                diff = prefix_sum[end]
            else:
                diff = prefix_sum[end] - prefix_sum[start - 1]

            result = max(result, diff % m)

    return result


print(maximumSum([3, 4, 5], 7))  # 6
# print(maximumSum([3, 3, 9, 9, 5], 7))  # 6