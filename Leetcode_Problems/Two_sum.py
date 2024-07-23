class Solution:
    def twoSum_1(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_2(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found
    
#       0 1 2 3 4 5
nums = [1,2,3,4,5,6]
target = 10

Test = Solution()
# print(Test.twoSum_1(nums, target))
print(Test.twoSum_2(nums, target))