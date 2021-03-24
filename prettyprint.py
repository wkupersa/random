
import numpy as pd
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        if A == 1:
            return [1]
        # Array is 2A - 1  by 2A -1
        arr =  pd.ones(((2*A-1),(2*A-1)),int)      
        n = 2*A-1
        for i in range(0,A):
            for j in range(i,n-i):
                arr[i,j] = A - i       
                arr[j,i] = A - i       
                arr[n-i-1,j] =  A - i
                arr[n-j-1,n-i-1] =  A - i
        return arr
test = Solution()
print(test.prettyPrint(1))