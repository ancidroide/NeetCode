class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # find total multiplication
        total_m = 1
        zeroes = 0
        contains_zero = False
        for num in nums:
            if num != 0:
                total_m *= num
            else:
                zeroes += 1
                contains_zero = True

        # build output array
        output = []
        for num in nums:
            if num == 0:
                if zeroes == 1:
                    output.append(total_m)
                else:
                    output.append(0)
            
            else:
                if contains_zero:
                    output.append(0)
                else:
                    current_value = total_m // num
                    output.append(current_value)

        return output
        