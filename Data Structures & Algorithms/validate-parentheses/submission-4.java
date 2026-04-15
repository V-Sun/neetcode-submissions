class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> pairings = new HashMap<>();
        pairings.put('(', ')');
        pairings.put('[', ']');
        pairings.put('{', '}');
        Stack<Character> stack = new Stack<>();
        for(char c: s.toCharArray()) {
            if(pairings.containsKey(c)) {
                stack.push(c);
                
            } else {
                if(stack.isEmpty() || pairings.get(stack.peek()) != c) {
                    return false;
                }
                stack.pop();
            }
        }

        return stack.isEmpty();

    }
}
