class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(l,h):
            while(l<=h):
                mid=(l+h)//2
                if nums[mid]>target:
                    h-=1
                if nums[mid]==target:
                    return mid
                if nums[mid]<target:
                    l+=1
            return -1
        return find(0,len(nums)-1)
        