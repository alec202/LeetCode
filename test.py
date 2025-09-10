def lengthOfLongestSubstring(s: str) -> int:
    ls = 0
    left = 0
    right = left + 1
    if len(s) < 2:
        return len(s)

    let_indx = {s[0]: 0}
    while right < len(s):
        new_lett = s[right]
        if new_lett in let_indx:
            new_l_index = let_indx[new_lett] + 1
            while left != new_l_index:
                let_indx.pop(s[left], "")
                left += 1
            let_indx[new_lett] = left
        else:
            let_indx[new_lett] = right
        right += 1
        ls = max(ls, len(let_indx))
    return ls
print(lengthOfLongestSubstring("aabaab!bb"))