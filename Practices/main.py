class Solution:
    # Mapping
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n : int = len(heights)
        # Create a dictionary to store the height and name
        mapping : dict[int, str] = {}

        # Loop through the list of names and heights
        for i in range(n):
            mapping[heights[i]] = names[i]

        # Using list.sort(reverse=False/True) to sort all elements in
        # the list in order (from smaller to bigger or versa)
        # In this case use True because we want sort name who has highest
        # height
        heights.sort(reverse=True)

        # Loop through the list of heights
        # Dictionary mapping can be accessed by using syntax
        # mapping[heihgts[index]] => return the name of the person who has
        for i in range(n):
            names[i] = mapping[heights[i]]
            
        return names

    # BubbleSort - Worst case scenario 
    def sortPeople_BubbleSort(self, names: list[str], heights: list[int]) -> list[str]:
        n : int = len(heights)
        for i in range(n):
            for j in range(0, n-i-1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
                    
        return names

    
    # SelectionSort
    def sortPeople_SelectionSort(self, names: list[str], heights: list[int]) -> list[str]:
        n : int = len(heights)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if heights[j] > heights[min_idx]:
                    min_idx = j

            heights[i], heights[min_idx] = heights[min_idx], heights[i]
            names[i], names[min_idx] = names[min_idx], names[i]

        return names
    
# names = ["Mary","John","Emma"]
# heights = [180,165,170]

# names = ["Alice","Bob","Bob"]
# heights = [155,185,150]

names = ["IEO","Sgizfdfrims","QTASHKQ","Vk","RPJOFYZUBFSIYp","EPCFFt","VOYGWWNCf","WSpmqvb"]
heights = [17233,32521,14087,42738,46669,65662,43204,8224]

Test = Solution()
print(Test.sortPeople_SelectionSort(names, heights))