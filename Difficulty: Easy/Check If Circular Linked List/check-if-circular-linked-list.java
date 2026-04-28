class Solution {
    boolean isCircular(Node head) {
        // code here
        if(head.next == null){
            return false;
        }
        Node temp = head.next;
        while(temp!=null && temp!=head){
            temp = temp.next;
        }
        if(temp == head){
            return true;
        }
        else{
            return false;
        }
        
        
    }
}