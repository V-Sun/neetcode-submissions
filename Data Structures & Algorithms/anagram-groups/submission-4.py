class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}

        for str in strs:
            freq = [0] * 26
            for c in str:
                freq[ord(c) - ord('a')] += 1
            
            key = tuple(freq)
            if key in my_map:
                my_map[key].append(str)
            else:
                my_map[key] = [str]

        res = []
        for key, value in my_map.items():
            res.append(value)
        
        return res