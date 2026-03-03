from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # check if nums[r] > nums[l]. If so, then just grab nums[l] and compare to current min because
        # that'd mean we have sorted array
        minSeen = nums[0]
        l = 0
        r = len(nums) - 1
        while (r >= l):
            if nums[r] > nums[l]:
                minSeen = min(minSeen, nums[l])
                break
            mid = l + (r - l) // 2
            minSeen = min(minSeen, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return minSeen

