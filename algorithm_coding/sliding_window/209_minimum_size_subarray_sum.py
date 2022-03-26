from typing import List

def minSubArrayLen(s: int, 
                   nums: List[int]) -> int:

    min_length = len(nums)
    l = r = 0
    local_sum = 0
    found = False

    for n in nums:

        # add the current number to local_sum
        local_sum += n
        
        # if local_sum >= s, keep decrement it till < s while updating min_length
        while local_sum >= s:
            found = True
            min_length = min(min_length, r-l+1)
            local_sum -= nums[l]
            l += 1

        # print(f'[{l},{r}]')

        # log r cursor
        r += 1

    if found == False:
        return 0
    else:
        return min_length


s = 7
nums = [2,3,1,2,4,3]

print(minSubArrayLen(s, nums))