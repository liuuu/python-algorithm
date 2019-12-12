from typing import List


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    my_dict = {}
    for i, v in enumerate(nums):
      if v in my_dict:
        return [my_dict[v], i]
      else:
        my_dict[target-v] = i
    return False


# find two number's sum equal to target
a = [1, 2, 3, 4, 34, 33, 7]
print(Solution().twoSum(a, 11))
