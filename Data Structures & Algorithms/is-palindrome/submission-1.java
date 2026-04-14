class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++) {
            char temp = s.charAt(i);
            if((temp - '0' >= 0 && temp - '9' <= 0) || (temp - 'a' >= 0 && temp - 'z' <= 0) || (temp - 'A' >= 0 && temp - 'Z' <= 0)) {
                sb.append(temp);
            }
        }
        String t = sb.toString().toLowerCase();
        int iter = t.length()/2;
        for(int i = 0; i < iter; i++) {
    
            if(t.charAt(i) != t.charAt(t.length() - 1 - i)) {
                return false;
            }
        }

        return true;
    }
}
