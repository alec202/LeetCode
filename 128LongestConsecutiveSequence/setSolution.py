class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bucket = set(nums)
        lcs = 0
        for num in bucket:
            if num - 1 not in bucket:
                sequenceLength = 1
                # if num - 1 not in bucket, then we know that this number is the start of a sequence.
                while num + sequenceLength in bucket:
                    sequenceLength += 1
                # no more nums in the sequence.
                lcs = max(sequenceLength, lcs)
        return lcs

