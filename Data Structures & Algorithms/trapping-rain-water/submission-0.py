class Solution:
    def trap(self, height: List[int]) -> int:
        l_m=[]
        r_m=[]
        m=0
        for i in height:
            m=max(m,i)
            l_m.append(m)
        m=0
        for i in range(len(height)-1,-1,-1):
            m=max(m,height[i])
            r_m.append(m)
        r_m.reverse()
        s=0
        for i in range(len(height)):
            s+=min(l_m[i],r_m[i])-height[i]
        return s
        
        