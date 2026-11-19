class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=defaultdict(int)
        l=0
        r=0
        m=0
        while(r<len(s)):
            if d[s[r]]>=1:
                d[s[l]]-=1
                l+=1
            else:
                d[s[r]]+=1
                r+=1
            m=max(m,r-l)
        return m     