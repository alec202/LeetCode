class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing order: smallest to biggest
        l, r = 0, len(numbers) - 1
        for i in range(0, len(numbers)):
            lSummedR = numbers[l] + numbers[r]
            if lSummedR == target:
                return [l + 1, r + 1]
            elif lSummedR < target:
                l += 1
            elif lSummedR > target:
                r -= 1


"""
numbers = [2, 11,15, 7]
target = 9
"""