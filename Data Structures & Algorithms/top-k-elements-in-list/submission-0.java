class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num: nums) {
            if(map.containsKey(num)) {
                int temp = (map.get(num)) + 1;
                map.put(num, temp);
            } else {
                map.put(num, 1);
            }
        }

        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int key = entry.getKey();
            int val = entry.getValue();
            pq.offer(entry);
        }

        int[] result = new int[k];
        for(int i = 0; i < k; i++) {
            result[i] = pq.poll().getKey();
        }

        return result;
    }
}
