class Solution:
    def visibleBuildings(self, arr):
        # code here
        maxi = float('-inf')
        ans = 0
        
        for num in arr:
            if maxi <= num:
                ans += 1
                maxi = max(maxi, num)
        
        return ans