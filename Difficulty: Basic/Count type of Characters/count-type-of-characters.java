// User function Template for Java

class Sol {
    int[] count(String s) {
        // your code here
        int upper = 0;
        int lower = 0;
        int special = 0;
        int num = 0;
        for(int i=0; i<s.length(); i++){
            char ch = s.charAt(i);
            if(ch>='A' && ch<='Z') upper++;
            else if(ch>='a' && ch<='z') lower++;
            else if(ch>='0' && ch<= '9') num++;
            else special++;
        }
        return new int[] {upper,lower,num,special};
    }
}