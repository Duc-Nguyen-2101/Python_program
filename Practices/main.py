class Solution:
    # def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        # n : int = len(heights)
        # # Create a dictionary to store the height and name
        # mapping : dict[int, str] = {}

        # # Loop through the list of names and heights
        # for i in range(n):
        #     mapping[heights[i]] = names[i]

        # # Using list.sort(reverse=False/True) to sort all elements in
        # # the list in order (from smaller to bigger or versa)
        # # In this case use True because we want sort name who has highest
        # # height
        # heights.sort(reverse=True)

        # # Loop through the list of heights
        # # Dictionary mapping can be accessed by using syntax
        # # mapping[heihgts[index]] => return the name of the person who has
        # for i in range(n):
        #     names[i] = mapping[heights[i]]
            
        # return names


    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n:int = len(heights)
        for i in range(n):
            for j in range(0, n-1-i):
                if heights[i] > heights[j]:
                    names[i], names[j] = names[i], names[j]
                    # heights[i], heights[j] = heights[i], heights[j]
                else:
                    names[i], names[j] = names[j], names[i]
                    # heights[i], heights[j] = heights[j], heights[i]
        
        return names
    
names = ["Mary","John","Emma"]
heights = [180,165,170]

Test = Solution()
print(Test.sortPeople(names, heights))