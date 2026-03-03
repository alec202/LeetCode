class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while (l <= r):
            mid = l + (r - l) // 2
            currentNum = nums[mid]
            if currentNum < target:
                l = mid + 1
            elif currentNum > target:
                r = mid - 1
            else:
                return mid
        else:
            return -1
