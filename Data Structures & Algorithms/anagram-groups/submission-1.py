class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = {}
        for s in strs:
            if ''.join(sorted(s)) in anagrams:
                anagrams[''.join(sorted(s))].append(s)
            else:
                anagrams[''.join(sorted(s))] = [s]
        
        for key in anagrams:
            result.append(anagrams[key])
        
        return result