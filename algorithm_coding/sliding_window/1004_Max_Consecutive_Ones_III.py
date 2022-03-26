"""
Question:

Given an array `arr` of 0s and 1s, we may change up to `k` numbers of 0s to 1s
so that we can have the longest consecutive subarray that contains only 1s.

For example:
    arr = [1,1,0,0,0,1,1,1,1,0]
    k = 2
We may flip the last two 0s from the right, to 1s, then the arr becomes:
    [1,1,0,0,1,1,1,1,1,1]
"""


def max_count(arr, k):
    l = 0
    r = 0
    zeros = 0
    max_count = 0

    for a in arr:
        if a == 0:
            zeros += 1

        # if we have more zeros than permitted; k, then we should reduce that down to the threshold. moving l
        while zeros > k:
            if arr[l] == 0:
                zeros -= 1
            l += 1

        # print(f'[{l},{r}]')
        max_count = max(max_count, r-l+1)
        r += 1

    return max_count


test_cases = [
    {'arr':[0,1,1,1,0,0,0,1,1,1,1,0], 'k':2, 'exp':6},
    {'arr':[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 'k':3, 'exp':10},
    {'arr':[0,0,0], 'k':3, 'exp':3},
    {'arr':[1,1,1,1], 'k':3, 'exp':4},
    {'arr':[0,1,0,0,1], 'k':0, 'exp':1},
]

for t in test_cases:
    arr = t['arr']
    k = t['k']
    exp = t['exp']
    
    print(exp == max_count(arr, k))
