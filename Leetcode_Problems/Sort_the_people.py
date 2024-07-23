class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n:int = len(heights)
        for i in range(n):
            for j in range(i, n-1):
                if heights[i] > heights[j]:
                    # names[i], names[j] = names[i], names[j]
                    heights[i], heights[j] = heights[i], heights[j]
                else:
                    # names[i], names[j] = names[j], names[i]
                    heights[i], heights[j] = heights[j], heights[i]
        
        return heights
    
# names = ["IEO","Sgizfdfrims","QTASHKQ","Vk","RPJOFYZUBFSIYp","EPCFFt","VOYGWWNCf","WSpmqvb"]
# names = ["1","2","3","4","5","6","7","8"]
# heights = [17233,32521,14087,42738,46669,65662,43204,8224]

names = ["Mary","John","Emma"]
heights = [180,165,170]

Test = Solution()

# Expected ["EPCFFt","RPJOFYZUBFSIYp","VOYGWWNCf","Vk","Sgizfdfrims","IEO","QTASHKQ","WSpmqvb"]
# Expected ["6", "5", "7", "4", "2", "1", "3", "8"]
print(Test.sortPeople(names, heights))