class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        m=float('-inf')
        s=0
        while i<len(nums):
            s+=nums[i]
            m=max(m,s)
            if s<0:
                s=0
            i+=1
        return m
        