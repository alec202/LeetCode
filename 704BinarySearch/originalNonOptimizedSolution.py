from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if target == nums[i]:
                return i
        return -1
