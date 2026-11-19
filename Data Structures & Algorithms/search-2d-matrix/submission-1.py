class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        def find(l,h,matrix):
            while l<=h:
                mid=(l+h)//2
                if matrix[mid]<target:
                    l+=1
                if matrix[mid]==target:
                    return True
                if matrix[mid]>target:
                    h-=1
            return False
        f=0
        for i in range(m):
            mi=matrix[i][0]
            ma=matrix[i][n-1]
            if mi<=target<=ma:
                f=1
                return find(0,n-1,matrix[i])  
        if f==0:
            return False      