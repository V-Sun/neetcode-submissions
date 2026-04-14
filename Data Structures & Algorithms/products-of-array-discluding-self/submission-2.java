class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        int[] result = new int[nums.length];

        int temp = 1;
        prefix[0] = 1;
        for(int i = 1; i < nums.length; i++) {
            temp *= nums[i-1];
            prefix[i] = temp;
        }

        temp = 1;
        suffix[nums.length -1] = 1;
        for(int i = nums.length-2; i >= 0; i--) {
            temp *= nums[i+1];
            suffix[i] = temp;
        }

        System.out.println(Arrays.toString(prefix));
        System.out.println(Arrays.toString(suffix));

        for(int i = 0; i < nums.length; i++) {
            result[i] = prefix[i] * suffix[i];
        }

        return result;

    }
}  
