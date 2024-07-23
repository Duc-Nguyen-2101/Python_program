class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n : int = len(heights)
        mapping : dict[int, str] = {}
        for i in range(n):
            mapping[heights[i]] = names[i]

        # Using list.sort(reverse=False/True) to sort all elements in
        # the list in order (from smaller to bigger or versa)
        # In this case use True because we want sort name who has highest
        # height
        
        heights.sort(reverse=True)
        return heights
    
names = ["Mary","John","Emma"]
heights = [180,165,170]

Test = Solution()
print(Test.sortPeople(names, heights))