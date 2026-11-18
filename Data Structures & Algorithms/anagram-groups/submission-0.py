class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h=defaultdict(list)
        for i in strs:
            sorteds=''.join(sorted(i))
            h[sorteds].append(i)
        return list(h.values())



        