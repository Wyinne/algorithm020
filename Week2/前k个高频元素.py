#法一
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_counts = Counter(nums)
        top_three = nums_counts.most_common(k)
        res=[]
        for i in top_three:
            res.append(i[0])
        return res


#法二
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        b=set(nums)
        hashtable=dict()
        for i in b:
            count=0
            for j in range(len(nums)):
                if i == nums[j]:
                    count+=1
                    j+=1
            hashtable[i]=count
        res=sorted(hashtable, key = hashtable.get,reverse=True)
        result=[]
        for i in range(k):
            for key, val in hashtable.items():
                if key == res[i]:
                    result.append(key)
        return result