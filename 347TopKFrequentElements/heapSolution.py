class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        from heapq import heapify, heappop
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        # we've built up our num_count dictionary
        arr_to_heap = []
        for key in num_count:
            arr_to_heap.append([-num_count[key], key])
        # built up our arr to heapify
        heapify(arr_to_heap)
        # heapify modifies list in place. for transparancy let's set heaped pointer to that same array.
        heaped = arr_to_heap
        r_list = []
        for i in range(0, k):
            r_list.append(heappop(heaped)[1])
        return r_list


