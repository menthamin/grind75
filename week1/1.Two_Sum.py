# https://leetcode.com/problems/two-sum/
# 해시테이블 사용

nums = [2, 7, 11, 15]
target = 9


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:

        LEN = len(nums)

        for i in range(LEN):
            for j in range(i + 1, LEN):
                if nums[i] + nums[j] == target:
                    return [i, j]


func = Solution()
func.two_sum(nums=nums, target=target)


# Wrong
class Solution2:
    def two_sum(self, nums: list[int], target: int) -> list[int]:

        for i, num in enumerate(nums):
            goal_num = target - num
            if goal_num in nums:
                return [i, nums.index(goal_num)]


func2 = Solution2()
func2.two_sum(nums=nums, target=target)


# Approach 3: One-pass Hash Table
class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[num] = i


func3 = Solution3()
func3.twoSum(nums=nums, target=target)
