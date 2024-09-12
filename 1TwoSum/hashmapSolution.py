class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 3:
            return [0, 1]
        else:
            vals_needed = {}
            for i in range(0, len(nums)):
                if nums[i] in vals_needed:
                    return [i, vals_needed[nums[i]]]
                else:
                    vals_needed[target - nums[i]] = i

# nums = [3,2,4]
# target = 6
# i = 2
# nums[i] = 4 
# vals_needed = { 3:0, 4: 1,}
