"""
给定一个integer 返回小于这个In‍‌‌‌‌‍‍‌‍‍‍‌‌‍‍‍‌‌‌teger的最大数
example: 1237468 --> 1236874"

corner case:
    1234

1237468
   ^^
   4768
   
Similar: https://leetcode.com/problems/next-permutation/ 
"""

class Solution:
    def previous_small(self, curr):
        
        curr = [int(x) for x in str(curr)]

        pivot = len(curr)
        if pivot <= 1:
            return curr 
        
        for i in range(len(curr)-1, 0, -1):
            if curr[i-1] > curr[i]:
                pivot = i-1
                break 

        print(pivot)

        if pivot == len(curr):
            return curr[::-1]
        
        pivot_val = curr[pivot]
        for i in range(len(curr)-1, -1, -1):
            if curr[i] < pivot_val:
                curr[i], curr[pivot] = curr[pivot], curr[i]
                break
        
        curr[pivot+1:] = curr[pivot+1:][::-1]

        return curr

print(Solution().previous_small(1237468))
