import collections

def characterReplacement(s: str, 
                         k: int) -> int:
    l = 0
    max_count = 0
    max_length = 0
    counter = collections.Counter()

    for r in range(len(s)):
        counter[s[r]] += 1
        current_char_count = counter[s[r]]
        max_count = max(max_count, current_char_count)

        if r - l - max_count + 1 > k:
            counter[s[l]] -= 1
            l += 1

        max_length = max(max_length, r-l+1)
        print(f'\n{l}:{r}=>{max_length}')
        print(counter)
    return max_length

##
## high vote answer:
##
def characterReplacement_2(s, k):
    count = {}
    max_count = start = result = 0
    for end in range(len(s)):
        count[s[end]] = count.get(s[end], 0) + 1
        max_count = max(max_count, count[s[end]])
        if end - start + 1 - max_count > k:
            count[s[start]] -= 1
            start += 1
        result = max(result, end - start + 1)
        print(f'{start}:{end}=>{result}')

    return result


print(characterReplacement('AABABBA', 1))