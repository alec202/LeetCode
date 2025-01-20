class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing order: smallest to biggest
        nums = {}
        for i in range(0, len(numbers)):
            nums[numbers[i]] = i
        # built up our dictionary
        for i in range(0, len(numbers)):
            remainder = target - numbers[i]
            if remainder in nums:
                return [i + 1, nums[remainder] + 1]


"""
numbers = [2, 11,15, 7]
target = 9
i = 0
j = 3
"""