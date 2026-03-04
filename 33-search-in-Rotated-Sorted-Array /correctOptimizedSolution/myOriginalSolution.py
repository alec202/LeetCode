from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            midNum = nums[mid]
            if midNum == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif r - l + 1 <= 3:
                return -1
            elif nums[l] == nums[r]:
                return l if nums[l] == target else -1
            elif nums[r] > nums[l]:
                if target < midNum:
                    r = mid - 1
                else:
                    l = mid + 1
            elif midNum > nums[l]: #left half sorted
                if nums[l] <= target < midNum:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[r] > midNum: # right half sorted
                if midNum < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return l if nums[l] == target else -1

x = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
res = x.search(nums, target)
print(res)