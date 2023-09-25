import time
from test_func import test
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        List = []
        for a, i in enumerate(nums):
            for b, j in enumerate(nums):
                if (i + j == target) and (i != j):
                    List.append(a)
                    List.append(b) 
                    return List

ist = [2, 7, 11, 15]
sample_1 = Solution()
sample_1.twoSum(ist, 9)


t0 = time.process_time()
test(sample_1.twoSum(nums = [2,7,11,15], target = 9) == [0, 1])
t1 = time.process_time_ns()
print(t1 - t0)
test(sample_1.twoSum(nums = [3,2,4], target = 6) == [1, 2])