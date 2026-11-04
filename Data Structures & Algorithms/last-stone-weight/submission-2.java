class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int i : stones){
            pq.add(i);
        }
        int x;
        int y;
        int res;
        while(pq.size() >= 2) {
            x = pq.poll();
            y = pq.poll();
            if(x == 0) {
                pq.add(0);
                break;
            }
            res = x - y;
            if(res < 0) {
                res *= -1;
            }
            pq.add(res);
        }
        return pq.peek();
    }
}
