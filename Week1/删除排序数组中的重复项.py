class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        while (j < len(nums)):
            if nums[i] < nums[j]:
                i += 1
                j += 1
            else:
                nums.pop(j)
                return len(nums)
a=Solution()
c=[0,0,1,1,1,1,1,1,1,2]
b=a.removeDuplicates(c)
print(b)