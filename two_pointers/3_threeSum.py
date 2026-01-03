class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # in-place sorting --> O(1) space
        triplets = []

        for i in range(len(nums) - 2):
            # remove duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L = i + 1 # pointer 1 from start
            R = len(nums) - 1 # pointer 2 from end
            t = -nums[i] # target --> a+b = c (-nums[i]) = 0

            while L < R:
                current_sum = nums[L] + nums[R]

                if current_sum == t: # triplet found
                    triplets.append([nums[i], nums[L], nums[R]])

                    # update L and R without duplicates
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                
                    L += 1
                    R -= 1

                elif current_sum < t:
                    L += 1
                else:
                    R -= 1

        return triplets