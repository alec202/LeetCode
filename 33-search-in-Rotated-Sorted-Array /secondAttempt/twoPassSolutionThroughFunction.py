class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        def binary_search(l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                # target in left half
                elif target < nums[mid]:
                    r = mid - 1
                # target in right half
                else:
                    l = mid + 1
            return - 1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        else:
            return binary_search(pivot, len(nums) - 1)
