class Solution {
    public boolean isPalindrome(String s) {
        String t = "";
        for(int i = 0; i < s.length(); i++) {
            char temp = s.charAt(i);
            if((temp - '0' >= 0 && temp - '9' <= 0) || (temp - 'a' >= 0 && temp - 'z' <= 0) || (temp - 'A' >= 0 && temp - 'Z' <= 0)) {
                t += temp;
            }
        }
        t = t.toLowerCase();
        System.out.println(t);
        int iter = t.length()/2;
        for(int i = 0; i < iter; i++) {
    
            if(t.charAt(i) != t.charAt(t.length() - 1 - i)) {
                return false;
            }
        }

        return true;
    }
}
