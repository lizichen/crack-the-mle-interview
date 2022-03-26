def count_consecutive(arr):

    if arr == None or len(arr) == 0:
        return 0

    max_count = 0
    local_count = 0

    for a in arr:
        if a == 1:
            local_count += 1
        else:
            local_count = 0
        max_count = max(local_count, max_count)
    
    return max_count
    
test_cases = [
    [0,1,1,1,0,1,1,1,0,1,0,0,0],
    [1,1,1],
    [0,0,0],
    [0],
    [1],
    [],
    None
]

for t in test_cases:
    result = count_consecutive(t)
    print(result)