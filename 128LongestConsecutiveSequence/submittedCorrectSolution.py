class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxVal = max(nums)
        bucket = {}
        for num in nums:
            bucket[num] = 1
        # now we've created our bucket dictionary, key is num from nums, value is number of occurrences of this num.
        lcs = 0
        currSeq = 0
        for num in nums:
            if num in bucket:
                currSeq += 1
                i = num - 1
                while i in bucket:
                    currSeq += 1
                    del bucket[i]
                    i -= 1
                # check right
                i = num + 1
                while i in bucket:
                    del bucket[i]
                    currSeq += 1
                    i += 1
                if currSeq > lcs:
                    if num in bucket: del bucket[num]
                    lcs = currSeq
                    currSeq = 0
                else:
                    if num in bucket: del bucket[num]
                    currSeq = 0
        return lcs


'''
nums = [100, 4, 200, 1, 3, 2]
bucket = {}
num = 200
i = 201
currseq = 0
lcs = 4
maxVal = 200
minVal = 100

'''


