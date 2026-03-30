class Solution {
    public boolean isAnagram(String s, String t) {
        ArrayList<String> set1 = new ArrayList<String>();
        ArrayList<String> set2 = new ArrayList<String>();
        for(int i = 0; i < s.length(); i++) {
            set1.add(s.substring(i, i+1));
        }
        for(int i = 0; i < t.length(); i++) {
            set2.add(t.substring(i, i+1));
        }
        Collections.sort(set1);
        Collections.sort(set2);
        return set1.equals(set2);
    }
}
