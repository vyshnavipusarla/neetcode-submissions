class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        m=0
        while i<j:
            if heights[i]<heights[j]:
                m=max(m,heights[i]*(j-i))
                i+=1
            else:
                m=max(m,heights[j]*(j-i))
                j-=1
        return m

        