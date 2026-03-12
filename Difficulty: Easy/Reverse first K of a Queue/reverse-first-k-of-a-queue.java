class Solution {
    public Queue<Integer> reverseFirstK(Queue<Integer> q, int k) {
        if(k<=0 || k>q.size()){
            return q;
        }
        Stack<Integer> st1 = new Stack<>();
        
        for (int i = 0; i < k; i++) {
            st1.push(q.remove());
        }
        while (!st1.isEmpty()) {
            q.add(st1.pop());
        }
        int rem = q.size() - k;
        for (int i = 0; i < rem; i++) {
            q.add(q.remove());
        }

        return q;
    }
}