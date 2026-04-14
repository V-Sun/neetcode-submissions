class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0) {
            return 0;
        }

        HashSet<Integer> set = new HashSet<>();

        for(int n: nums) {
            set.add(n);
        }

        List<Integer> starts = new ArrayList<>();
        for(int n: nums) {
            if(!set.contains(n-1)) {
                starts.add(n);
            }
        }
        int maximum = 1;
        for(int n: starts) {
            int temp = 0;
            while(set.contains(n)) {
                n++;
                temp++;
            }

            maximum = Math.max(maximum, temp);
        }

        return maximum;
        
    }
}
