class Solution:
    def canSplit(self, arr):
        #code here
        sm=sum(arr)
        if sm%2!=0:
            return False
        curr=0
        for i in arr:
            curr+=i
            if curr==sm//2:
                return True
        return False