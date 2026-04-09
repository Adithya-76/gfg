class Solution {
    public static int distributeTicket(int N,int K)
    {
        int left = 1;
        int right = N;
        
        while(left<right){
            if(left+K > right){
                return right;
            }
            left+=K;
            
            if(right-K < left){
                return left;
            }
            right-=K;
            
        }
        return left;
    }
}