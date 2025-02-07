from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        # list is bigger than 3 items
        sumsFound = []
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            prevl = ''
            prevr = ''
            while l < r:
                if prevl == nums[l]:
                    l += 1
                    continue
                elif prevr == nums[r]:
                    r -= 1
                    continue
                numsSum = nums[i] + nums[l] + nums[r]
                if numsSum == 0:
                    sumsFound.append([nums[i], nums[l], nums[r]])
                    prevl = nums[l]
                    prevr = nums[r]
                    l += 1
                    r -= 1
                elif numsSum > 0:
                    prevr = nums[r]
                    r -= 1
                elif numsSum < 0:
                    prevl = nums[l]
                    l += 1
        return sumsFound

"""
nums = [-1,0,1,2,-1,-4]
numsSorted = [-4, -1, -1, 0, 1, 2]
nums[i] = -1
nums[l] = 0
nums[r] = 1
prevl = -1
prevr = 2
numsSum = 
sumsFound = {(-1, -1, 2), (-1, 0, 1)}
"""