class Solution:

    def maxArea(self,heights):
        largest = 0
        for i, x1 in enumerate(heights):
            for j in range(i+1, len(heights)):
            
                height = min(x1,heights[j])
                current = ((j-i) * height)
                if current > largest:
                    largest = current
        return largest

test = Solution()
print(test.maxArea([1,1]))