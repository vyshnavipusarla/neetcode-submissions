class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        cur=nums[0]
        i=1
        s=0
        m=0
        while i<len(nums):
            if cur==nums[i]:
                i+=1
            elif nums[i]==cur+1:
                cur=nums[i]
                i+=1
                s+=1
                m=max(m,s)
            else:
                cur=nums[i]
                i+=1
                s=0
        return m+1




        