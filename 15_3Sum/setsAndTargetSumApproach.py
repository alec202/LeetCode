from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        neg, pos, zero = [], [], []
        for num in nums:
            if num < 0:
                neg.append(num)
            elif num > 0:
                pos.append(num)
            else:
                zero.append(num)
        # we have our list of integers.
        if len(zero) > 2:
            res.add((0, 0, 0))
        negg = set(neg)
        poss = set(pos)
        zeros = set(zero)
        # checks all negative numbers for their complement with 0 added together
        if zeros:
            for n in negg:
                if -1*n in poss:
                    res.add((n, 0, n*-1))
        # pick two negative numbers, add them together, and see if their complement is in the positive set.
        for i in range(0, len(neg)):
            for j in range(i + 1, len(neg)):
                x = neg[i]
                y = neg[j]
                summed = x + y
                if -1 * summed in poss:
                    sortedSol = [x, y, -1 * summed]
                    sortedSol.sort()
                    sortedSol = tuple(sortedSol)
                    if sortedSol not in res:
                        res.add(sortedSol)

        # pick two positive numbers, add them together, and see if their complement is in the negative set.
        for i in range(0, len(pos)):
            for j in range(i + 1, len(pos)):
                x = pos[i]
                y = pos[j]
                summed = x + y
                if -1 * summed in negg:
                    sortedSol = [x, y, -1 * summed]
                    sortedSol.sort()
                    sortedSol = tuple(sortedSol)
                    if sortedSol not in res:
                        res.add(sortedSol)
        return [list(sol) for sol in res]

"""
nums = [-1,0,1,2,-1,-4]
neg = [-1, -1, -4]
zero = [0]
pos = [1, 2]
negg = {-1, -4}
zeros = {0}
poss = {1, 2}
res = {(-1, 0, 1), }
"""
