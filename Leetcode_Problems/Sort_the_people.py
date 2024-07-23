class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n:int = len(heights)
        for i in range(n):
            for j in range(0, n-i-1):
                if heights[j] < heights[j+1]:
                    names[j], names[j+1] = names[j+1], names[j]
                    heights[j], heights[j+1] = heights[j+1], heights[j]
        
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