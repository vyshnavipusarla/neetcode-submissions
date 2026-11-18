class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        l=[]
        for i in range(len(numbers)):
            if target-numbers[i] in seen:
                l.append(seen[target-numbers[i]]+1)
                l.append(i+1)
            seen[numbers[i]]=i
        return l

        