class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0) {
            return 0;
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int n: nums) {
            pq.offer(n);
        }
        int maximum = 1;
        int count = 1;
        int prev = pq.poll();
        for(int i = 0; i < nums.length - 1; i++) {
            int curr = pq.poll();
            if(curr == prev) {
                continue;
            } else if(curr - 1 == prev) {
                count++;
                maximum = Math.max(maximum, count);
            } else {
                maximum = Math.max(maximum, count);
                count = 1;
            }
            prev = curr;
        }

        return maximum;
        
        /*
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int n: nums) {
            if(map.containsKey(n-1)) {
                map.put(n, map.get(n-1) + 1);
            } else {
                map.put(n, 1);
            }
        }
        int maximum = Integer.MIN_VALUE;
        for(int n: map.values()) {
            maximum = Math.max(maximum, n);
        }

        return maximum;
        */
    }
}
