# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword in d:
                d[sortedword].append(word)
            else:
                d[sortedword] = [word]
        return list(d.values())
