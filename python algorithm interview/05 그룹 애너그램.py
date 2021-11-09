from collections import defaultdict
from collections import Counter


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)

        for str in strs:
            key = "".join(sorted(str))
            anagrams[key].append(str)

        # for str in strs:
        #     key = tuple(sorted(Counter(str).items()))
        #     anagrams[key].append(str)

        # return [value for value in anagrams.values()]
        # return list(anagrams.values())
        return anagrams.values()


sol = Solution()
print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
