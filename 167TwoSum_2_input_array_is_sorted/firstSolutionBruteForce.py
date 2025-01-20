class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # non-decreasing order: smallest to biggest
        for i in range(0, len(numbers)):
            for j in range(i + 1, len(numbers)):
                if j == i:
                    continue
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
   
"""
numbers = [2, 11,15, 7]
target = 9
i = 0
j = 3
"""
