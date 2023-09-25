import time
from test_func import test
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_1 = nums
        nums_1.sort()
        print(nums_1)
        end_ind = len(nums) - 1
        start_ind = 0
        while start_ind < end_ind:
            if ((nums_1[start_ind] + nums_1[end_ind]) > target):
                for i in range(start_ind + 1):
                    if (nums_1[i] + nums_1[end_ind] == target):
                        return [i, end_ind]
                for i in range(end_ind, len(nums_1)):
                    if (nums_1[start_ind] + nums_1[i]) == target:
                        return [start_ind, i]

            if (nums_1[start_ind] + nums_1[end_ind] == target):
                return [start_ind, end_ind]
            start_ind += 1
            end_ind -= 1

ist = [2, 7, 11, 15]
sample_1 = Solution()
sample_1.twoSum(ist, 9)


t0 = time.process_time()
test(sample_1.twoSum(nums = [2,7,11,15], target = 9) == [0, 1])
t1 = time.process_time_ns()
print(t1 - t0)
test(sample_1.twoSum(nums = [3,2,4], target = 6) == [1, 2])