class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedDict = {}
        for i in nums:
            if i in sortedDict:
                sortedDict[i] += 1
            else:
                sortedDict[i] = 1
        sorted_by_value = dict((sorted(sortedDict.items(), key=lambda item: item[1], reverse = True)))
        key_list = list(sorted_by_value.keys())
        output = []
        for i in range (k):
            output.append(key_list[i])
        return (output)