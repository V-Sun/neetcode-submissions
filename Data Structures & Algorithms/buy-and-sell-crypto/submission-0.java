class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length < 1) {
            return 0;
        }
        int prev = prices[0];
        int curr;
        int localMin = prices[0];
        int biggestGap = 0;
        for(int i = 1; i < prices.length; i++) {
            
            curr = prices[i];
           
            if(curr < prev) {
                biggestGap = Math.max(biggestGap, prev - localMin);
                
            } 
            localMin = Math.min(localMin, curr);
            prev = curr;        
        }

        biggestGap = Math.max(biggestGap, prev - localMin);
        return biggestGap;
    }
}
