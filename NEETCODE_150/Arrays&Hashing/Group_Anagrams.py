#HASH MAP

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HashMap = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 
            
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            HashMap[tuple(count)].append(s)
            
        return HashMap.values()