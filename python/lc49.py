import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for s in strs:
            re = "".join(sorted(s))
            mp[re].append(s)
        return list(mp.values())
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
#[["bat"],["nat","tan"],["ate","eat","tea"]]