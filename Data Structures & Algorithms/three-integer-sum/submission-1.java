class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i++) {
            int j = i+1;
            int k = nums.length - 1;


            while(j < k) {
                if(j == i) {
                    j++;
                    continue;
                }

                if(k == i) {
                    k--;
                    continue;
                }
                if(nums[j] + nums[k] + nums[i] == 0) {
                    List<Integer> temp = new ArrayList<>();
                    temp.add(nums[j]);
                    temp.add(nums[i]);
                    temp.add(nums[k]);
                    Collections.sort(temp);
                    if(!result.contains(temp)) {
                        result.add(temp);
                    }
                    j++;
                    k--;
                }
                if(nums[j] + nums[k] + nums[i] > 0) {
                    k--;
                } else if(nums[j] + nums[k] + nums[i] < 0) {
                    j++;
                }
            }
        }
        return result;
        
    }
}
