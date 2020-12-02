class Solution(object):
    def moveZeroes(self,nums):
        j=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
                i+=1
        return nums
a=Solution()
b=[0,1,0,12,3]
c=a.moveZeroes(b)
print(c)
