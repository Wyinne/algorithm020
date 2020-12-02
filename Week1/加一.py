class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        k=len(digits)
        for i in range(k):
            num+=digits[i]*10**(k-i-1)
        digits=[]
        if num==0:
            for i in range(k):
                digits.append(0)
            digits[-1]=1
        else:
            num+=1
            num=str(num)
            for i in range(len(num)):
                digits.append(int(num[i]))
        return digits