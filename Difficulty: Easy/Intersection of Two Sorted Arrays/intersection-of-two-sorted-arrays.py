class Solution:
    def intersection(self,a, b):
        # code here
        res = list(set(a).intersection(set(b)))
        res.sort()
        return res