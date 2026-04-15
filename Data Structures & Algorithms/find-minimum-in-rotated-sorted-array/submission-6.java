class Solution {
    public int findMin(int[] nums) {
        if(nums.length < 2) {
            return nums[0];
        } else if(nums.length < 3) {
            return Math.min(nums[0], nums[1]);
        }
        int start = 0; 
        int end = nums.length - 1;
        while(start <= end) {
            int mid = start + (end - start)/2 + 1;
            if(mid == start) {
                break;
            }
            System.out.println(start + " " + mid + " " + end);
            if(nums[mid-1] > nums[mid]) {
                return nums[mid];
            } else if(nums[mid] > nums[end]) {
                start = mid;
            } else {
                end = mid - 1;
            }
        }

        System.out.println("Did not find anything");
        return nums[0];
    }
}
