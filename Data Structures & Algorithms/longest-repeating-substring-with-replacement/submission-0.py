class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        f=defaultdict(int)
        res=0
        while r<len(s):
            f[s[r]]+=1
            m=max(f.values())
            length=r-l+1
            if length-m>k:
                f[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res



        