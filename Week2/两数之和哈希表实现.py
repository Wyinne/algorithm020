class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable=dict()
        for i ,num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num],i]
            hashtable[nums[i]]=i
        return []
a=Solution()
b=[2,5,5,11]
c=a.twoSum(b,10)
print(c)
