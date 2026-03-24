class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            #left half sorted
            elif nums[l] <= nums[mid]:
                # target in left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right half sorted
            else:
                # target in right half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                # target in left half
                else:
                    r = mid - 1
        return -1


"""
nums = [7, 1, 3]
target = 4
l = 2
r = 2
mid = 2

"""
