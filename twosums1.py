class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Sort the list to use two pointers
        sorted_nums = sorted(nums)
        start_index = 0
        end_index = len(sorted_nums) - 1
        
        # Iterate through the list using two pointers
        while start_index < end_index:
            current_sum = sorted_nums[start_index] + sorted_nums[end_index]
            if current_sum == target:
                # Find the indices of the two numbers in the original list
                index1 = nums.index(sorted_nums[start_index])
                index2 = nums.index(sorted_nums[end_index])
                if index1 == index2:
                    # If the two numbers are the same, find the index of the second occurrence
                    index2 = nums.index(sorted_nums[end_index], index1 + 1)
                return [index1, index2]
            elif current_sum < target:
                start_index += 1
            else:
                end_index -= 1
        
        # If no pair is found, return an empty list
        return []

mylist1 = [1,3,4,6,7,8,9,21, 56, 43, 32, 53, 23, 67, 24, 67, 14, 25]
ist = [2, 7, 11, 15]
sample_1 = Solution()
print(sample_1.twoSum(ist, 9))
print(sample_1.twoSum(mylist1, 55))
print(mylist1.index(23), mylist1.index(32))