class Solution {
    public int characterReplacement(String s, int k) {
        if(s.length() < 1) {
            return 0;
        }
        int start = 0;
        int end = 1;
        int totalMax = 1;
        while(end < s.length()) {
            int[] freq = new int[26];
            int maxFreq = 0;
            for(char c: s.substring(start, end+1).toCharArray()) {
                int idx = (c - 'A');
                freq[idx] += 1;
            }
            
            for(int c: freq) {
                maxFreq = Math.max(c, maxFreq);
            }

            if(k < ((end - start + 1) - maxFreq)) {
                start++;
            } else {
                totalMax = Math.max(totalMax, (end - start + 1));
                end++;
            }

        }

        return totalMax;
    }
}
