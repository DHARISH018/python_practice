class Solution:
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            value=nums[i]
            diff=target-value
            if value not in d:
                d[diff]=i
            else:
                current_index=i
                previous=d[value]
                return [previous,current_index]
nums = list(map(int, input("Enter the numbers (space-separated): ").split()))
target = int(input("Enter the target: "))

sol = Solution()
result = sol.twoSum(nums, target)

print("Indices of numbers that add up to target:", result)