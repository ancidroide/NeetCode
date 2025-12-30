class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        result = []
        for i in range(len(nums)):
            num_map[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in num_map and num_map[difference] != i:
                result.append(i)
                result.append(num_map[difference])
                return result

