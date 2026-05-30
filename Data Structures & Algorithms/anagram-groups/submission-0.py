from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for string in strs:
            key = tuple(sorted(Counter(string).items()))
            dic[key].append(string)
            
        return list(dic.values())