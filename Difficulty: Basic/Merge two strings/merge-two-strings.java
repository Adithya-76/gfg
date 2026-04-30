class Solution {
    String merge(String s1, String s2) {
        // code here
        
        StringBuilder result = new StringBuilder();
        int i =0 , j = 0;
        while(i<s1.length() && j<s2.length()){
            result.append(s1.charAt(i++));
            result.append(s2.charAt(j++));
   }
   while(i<s1.length()){
       result.append(s1.charAt(i++));
   }
   while(j<s2.length()){
       result.append(s2.charAt(j++));
   }
   
   
        return result.toString();
    }
}