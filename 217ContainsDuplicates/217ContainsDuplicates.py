from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_nums = {}
        for num in nums:
            val = seen_nums.get(num, 0) + 1
            if val == 1:
                seen_nums[num] = val
            else:
                return True
        return False