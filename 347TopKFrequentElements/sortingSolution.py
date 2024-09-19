class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        # we've built up our num count dictionary
        num_occs = []
        for num in num_count:
            num_occs.append([num_count[num], num])
        #built up our list of lists
        sorted_list = sorted(num_occs, key=lambda item: item[0], reverse=True)
        #now we have our sorted list
        r_list = []
        for i in range(0, k):
            r_list.append(sorted_list[i][1])
        return r_list

