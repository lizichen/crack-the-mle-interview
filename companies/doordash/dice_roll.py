"""
https://leetcode.com/discuss/interview-question/1515046/DoorDash-Data-Eng-Tech-phone-screen

"""

result = []

def dice_roll(n):
    helper(n, [])
    return result
    
def helper(n, tmp):
    if n == 0:
        result.append(tmp)
    else:
        for i in range(1, 7):
            helper(n-1, tmp+[i])
