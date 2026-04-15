class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length() < 1) {
            return 0;
        }
        int largest = 1;
        Map<Character, Integer> set = new HashMap<>();
        for(int x = 0; x < s.length(); x++) {
            if(set.containsKey(s.charAt(x))) {
                largest = Math.max(largest, set.size());
                int tempidx = set.get(s.charAt(x));
                set.remove(s.charAt(x));
                String temp = "";
                for(Map.Entry<Character, Integer> entry: set.entrySet()) {
                    if(entry.getValue() < tempidx) {
                        temp += entry.getKey();
                    }
                }
                
                for(char c: temp.toCharArray()) {
                    set.remove(c);
                }
                set.put(s.charAt(x), x);
            } else {
                set.put(s.charAt(x), x);
            }
        }

        largest = Math.max(set.size(), largest);
        return largest;


    }
}
