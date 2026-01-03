class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        # L < R and NOT L <= R --> index1 has to be != index2
        while L < R:
            numbers_sum = numbers[L] + numbers[R]
            index1 = L + 1
            index2 = R + 1
            index_list = [index1, index2]
            
            if numbers_sum == target:
                return index_list
            
            elif numbers_sum > target:
                R -= 1
                continue

            elif numbers_sum < target:
                L += 1
                continue
        
        return False