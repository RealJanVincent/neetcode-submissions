class KthLargest {
    
    private int k;
    private PriorityQueue<Integer> pq;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        pq = new PriorityQueue<>();
        for(int i : nums) {
            pq.add(i);
        }
    }
    
    public int add(int val) {
        pq.add(val);
        while(pq.size() > k) {
            pq.poll();
        }
        return pq.peek();
    }
}
