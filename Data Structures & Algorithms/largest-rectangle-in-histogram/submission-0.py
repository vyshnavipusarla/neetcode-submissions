class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        nse=[n]*n
        pse=[-1]*n
        st=[]
        for i in range(n):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            if st:
                pse[i]=st[-1]
            st.append(i)
        st=[]
        for i in range(n-1,-1,-1):
            while st and heights[st[-1]]>heights[i]:
                st.pop()
            if st:
                nse[i]=st[-1]
            st.append(i)
        m=float('-inf')
        for i in range(n):
            w=nse[i]-pse[i]-1
            h=heights[i]
            m=max(m,w*h)
        return m        