class Solution {

    public String encode(List<String> strs) {
        String result = "";
        for(String str: strs) {
            result += str.length() + "#" + str;
        }
        return result;
    }

    public List<String> decode(String str) {
        List<String> myList = new ArrayList<String>();
        int idx = 0;
        while(idx < str.length()) {
            String temp = "";
            while(str.charAt(idx) != '#') {
                temp += str.charAt(idx++);
            }
            idx++;
            int amount = Integer.parseInt(temp);
            myList.add(str.substring(idx, idx+amount));
            idx += amount;
            
            System.out.println(idx);
        }

        return myList;
        
    }
}
