// User function Template for Java

class Solution {
    int minValue(String S, int K) {
        // code here
        int[] freq = new int[26];
        int ans = 0;
        for(int i = 0; i<S.length(); i++){
            freq[S.charAt(i)-'a']++;
        }
        for(int i =0;i<K;i++){
            int p = 0;
            for(int j=0;j<26;j++){
                p = (freq[j]>freq[p]) ? j : p;
            }
            freq[p]--;
        }
        for(int i = 0; i<26; i++){
            if(freq[i]>0){
                ans +=freq[i]*freq[i];
            }
        }
        return ans;
    }
}