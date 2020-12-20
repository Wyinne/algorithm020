class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=list(s)
        b=list(t)
        for i in range(len(a)):
            a[i]=ord(a[i])
        a.sort()
        for i in range(len(b)):
            b[i]=ord(b[i])
        b.sort()
        return a==b