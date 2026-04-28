class Solution {
    public int maxProduct(int[] nums) {
        int maximum = 1;
        int minimum = 1;
        int total = nums[0];
        for(int num: nums) {
            int temp = num * maximum;
            maximum = Math.max(Math.max(num, num * minimum), num * maximum);
            minimum = Math.min(Math.min(num, temp), num * minimum);
            total = Math.max(total, maximum);
        }

        return total;
    }
}
