class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxVal = max(nums)
        bucket = {}
        for num in nums:
            bucket[num] = 1
        # now we've created our bucket dictionary, key is num from nums, value is number of occurrences of this num.
        print(bucket)
        minVal = min(nums)
        lcs = 0
        currSeq = 0
        for i in range(minVal, maxVal + 2):
            if i not in bucket:
                if currSeq > lcs:
                    lcs = currSeq
                    currSeq = 0
                else:
                    currSeq = 0
                # otherwise do nothing because lcs is longer than currSeq.
            else:
                currSeq += bucket[i]
        return lcs


'''
nums = [100,4,200,1, 2, 4, 5, 6]
currseq = 4
i = 4
lcs = 2
maxVal = 200
minVal = 100

'''


