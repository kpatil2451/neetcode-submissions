class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputMap = {}

        for i in strs:
            key = "".join(sorted(i))
            if key in outputMap:
                outputMap[key].append(i)
            else:
                outputMap[key] = [i]
        return list(outputMap.values())