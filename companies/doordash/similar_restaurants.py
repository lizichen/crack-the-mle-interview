# 原题：similar restaurants, 输入name: hotpot, array = ""hptoot, ""hoptot"", 
# 最多有k对character可以换，求输出list of string of similar restaurants
# Similar to 1347. Minimum Number of Steps to Make Two Strings Anagram
"""
hotpot <> hqtpot

h1 > 0
o2 > 1
t2 > 0
p1 > 0
"""

import collections

def calc_diff(r_name, r_len, name):
    diff = 0
    name_counter = collections.Counter(name)
    
    for ch in r_name:
        remain = r_name[ch] - name_counter[ch]
        if remain > 0:
            diff += remain
        
    print(name, diff)
    return diff

def similar_restaurants(r_name, name_list, allowed_diff):
    
    r_len = len(r_name)
    r_name = collections.Counter(r_name)
    
    result = []
    for name in name_list:
        if r_len == len(name) and calc_diff(r_name, r_len, name) <= allowed_diff:
            result.append(name)
    
    return result
    

# test:
r_name = 'hotpot'
name_list = [
    'hoptot', 'hotpot', 'oottph', # no diff
    'hptpot', 'hot1ot', 'httpot', # 1 char diff
    'h12pot', 'h12pot', 'httptt', # 2 chars diff
    'h123ot', '312pot', 'hokkok', # 3 chars diff
]
allowed_diff = 2

similar_restaurants(r_name, name_list, allowed_diff)
