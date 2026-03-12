class Solution:
    def deleteMid(self, stack):
        #code here
        n = len(stack)-1
        stack.pop(n//2)
        return stack