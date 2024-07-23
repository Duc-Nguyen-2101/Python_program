class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n: int = len(names)
        mapping: dict[int, str] = {}  # height -> name (heights are distinct)
        for ind in range(n):
            mapping[heights[ind]] = names[ind]

        heights.sort(reverse=True)
        for ind in range(n):
            h: int = heights[ind]
            names[ind] = mapping[h]

        return names
    
names = ["Mary","John","Emma"]
heights = [180,165,170]

Test = Solution()
print(Test.sortPeople(names, heights))