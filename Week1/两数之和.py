class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag=0
        for j in range(len(nums)):
            for i in range(len(nums)):
                if(target==nums[i]+nums[j]):
                    if (i+j!=flag) and i!=j:
                        return [j,i]
                    else:
                        i+=1
                    flag = i + j
#O(N)=T(N^2)
a=Solution()
b=[2,5,5,11]
c=a.twoSum(b,10)
print(c)

