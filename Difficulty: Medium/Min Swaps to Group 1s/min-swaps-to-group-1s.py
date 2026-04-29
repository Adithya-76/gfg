class Solution:
    def minSwaps(self, arr):
        ttl = sum(arr)
        if ttl==0: return -1
        n = len(arr)
        ans = 0
        s = 0
        curr_ttl = sum(arr[:ttl])
        for e in range(ttl, n):
            ans = max(ans, curr_ttl)
            curr_ttl += arr[e]
            curr_ttl -= arr[s]
            s += 1
        ans = max(ans, curr_ttl)
        return ttl-ans
        