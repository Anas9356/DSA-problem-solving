# my brute force : pass 28 test cases 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = k - 1
        Mx = float("-inf")
        flag = 0
        reslt = list()
        while end < len(nums):
            if flag == 1:
                flag = 0
                end += 1
                start += 1
                continue
            temp = start
            while temp <= end:
                Mx = max(nums[temp], Mx)
                temp += 1
            reslt.append(Mx)
            Mx = float("-inf")
            end += 1
            start += 1
            if end < len(nums):
                if nums[end] >= reslt[-1]:
                    reslt.append(nums[end])
                    print(reslt)
                    flag = 1

        return reslt
# 2nd optimize version which pass 48 out of 52
class Solution:
    def maxSlidingWindow(self, nums, k):
        start = 0
        end = k - 1
        res = []

        # initial max
        curr_max = max(nums[start:end+1])
        res.append(curr_max)

        while end < len(nums) - 1:
            start += 1
            end += 1

            # If outgoing element was max → recompute
            if nums[start - 1] == curr_max:
                curr_max = max(nums[start:end+1])
            else:
                curr_max = max(curr_max, nums[end])

            res.append(curr_max)

        return res
#optimize version of it 

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # stores indexes
        res = []

        for i in range(len(nums)):

            # Remove elements out of window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Start adding result after first window
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
