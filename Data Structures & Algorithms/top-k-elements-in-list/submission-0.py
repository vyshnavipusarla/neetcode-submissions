class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for i in range(len(nums)):
            if nums[i] not in f:
                f[nums[i]] =1
            else:
                f[nums[i]]+=1
        f=dict(sorted(f.items(),key=lambda item:item[1],reverse=True))
        l=[]
        for i,j in f.items():
            l.append(i)
        return l[:k]


        