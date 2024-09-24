from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        # make our dictionary holding the count we see each num
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        # constructed our dictionary with num count
        bucket_sort = [[] for i in range(0, len(nums) + 1)]
        # made our bucket
        for num in num_count:
            bucket_sort[num_count[num]].append(num)
        # created and filled our bucket
        return_arr = []
        for i in range(len(bucket_sort) - 1, 0, -1):
            while len(bucket_sort[i]) != 0 and len(return_arr) != k:
                return_arr.append(bucket_sort[i].pop())
            if len(return_arr) == k:
                return return_arr
        return return_arr