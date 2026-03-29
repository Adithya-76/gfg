class Solution:
    def countPartitions(self, arr, diff):
        tot=sum(arr)
        if (tot-diff)%2==1:
            return 0
        tar=(tot-diff)//2
        arr.sort()
        from functools import cache
        @cache
        def dp(ix=len(arr)-1,sm=0):
            nonlocal arr,tar
            if sm>tar:
                return 0
            if ix<0:
                return sm==tar
            ret=dp(ix-1,sm)+dp(ix-1,sm+arr[ix])
            return ret
        return dp()