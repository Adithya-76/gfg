class Solution:
    def commonElements(self, a, b, c):
        # code here
       a=set(a)
       b=set(b)
       c = set(c)
       res = []
       for i in a:
           if i in b and i in c:
               res.append(i)
       return sorted(res)