class Solution:
    def maxArea(self,height):
        i, j, maxi = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                maxi = max(maxi, height[i] * (j - i))
                i += 1
            else:
                maxi = max(maxi, height[j] * (j - i))
                j -= 1
        return maxi
a=Solution()
b=[1,8,6,2,5,4,8,3,7]
c=a.maxArea(b)
print(c)
