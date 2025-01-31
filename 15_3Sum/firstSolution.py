class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        # list is bigger than 3 items
        sumsFound = set()
        nums.sort()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sumsFound.add((nums[i], nums[j], nums[k]))
        output = []
        for vals in sumsFound:
            output.append(list(vals))
        return output

"""
nums = [-1,0,1,2,-1,-4]
numsSorted = [-4, -1, -1, 0, 1, 2]
nums[i] = -1
nums[j] = 0
nums[k] = 1
sumsFound = {(-1, -1, 2), (-1, 0, 1)}
"""