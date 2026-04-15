class Solution {
    public int maxArea(int[] heights) {
        int result = 0;
        int i = 0; 
        int j = heights.length - 1;
        while(i < j) {
            result = Math.max(Math.min(heights[i], heights[j]) * (j - i), result);
            if(heights[i] < heights[j]) {
                i++;
            } else  {
                j--;
            }
        }

        return result;
    }
}
