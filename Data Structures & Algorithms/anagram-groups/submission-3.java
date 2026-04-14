class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> mymap = new HashMap<>();
        for(String s: strs) {
            int[] sig = new int[26];
            
            for(char c: s.toCharArray()) {
                sig[c - 'a'] += 1;
            }
            String signature = "";
            for(int i: sig) {
                signature += i + "#";
            }
            if(mymap.containsKey(signature)) {
                ArrayList<String> temp = mymap.get(signature);
                temp.add(s);
            } else {
                ArrayList<String> temp = new ArrayList<>();
                temp.add(s);
                mymap.put(signature, temp);
            }
        }
        List<List<String>> result = new ArrayList<>();
        for(List<String> arr: mymap.values()) {
            result.add(arr);
        }
        return result;
    }
}
