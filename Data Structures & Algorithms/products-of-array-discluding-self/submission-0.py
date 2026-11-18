class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c_z=0
        t=1
        for i in nums:
            if i==0:
                c_z+=1
            else:
                t*=i
        if c_z>1:
            return [0]*len(nums)
        elif c_z==0:
            l=[]
            for i in nums:
                l.append(t//i)
            return l
        else:
            l=[]
            for i in nums:
                if i!=0:
                    l.append(0)
                else:
                    l.append(t)
            return l

            
            

        