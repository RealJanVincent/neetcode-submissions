class Solution {
    private double dist(int[] p) {
        return Math.sqrt((p[0] * p[0] + p[1] * p[1]));
    }

    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> Double.compare(dist(a), dist(b))
        );
        int[][] toReturn = new int[k][2];
        for(int[] p : points) {
            pq.add(p);
        }
        for(int i = 0; i < k; i++) {
            toReturn[i] = pq.poll();
        }
        return toReturn;
    }
}
