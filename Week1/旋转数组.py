#方法一 求余切片自己做的
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a= len(nums)-k%len(nums)
        nums.extend(nums[0:a])
        del nums[0:a]
        return nums
#方法二 插入数组末尾弹出的数 看的别人的题解
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for i in range(k):
            nums.insert(0, nums.pop())
#方法三 三次反转
class Solution:
    class Solution(object):
        def rotate(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: None Do not return anything, modify nums in-place instead.
            """
            n = len(nums)
            k %= n
            nums[:] = nums[::-1]
            nums[:k] = nums[:k][::-1]
            nums[k:] = nums[k:][::-1]
b=[2,5,5,11]
c=b.rotate(b,5)
print(c)