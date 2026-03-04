class Solution:
    def findUnion(self, a, b):
        # code here 
       a = a + b
       a = list(set(a))
       a.sort()
       return a
       