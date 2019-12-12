from typing import List

# backtracking


class Solution:
  def permutation(self, nums: List[int]) -> List[int]:
    ret = []

    def permutationHelper(start):
      if(start == len(nums) - 1):
        ret.append(nums.copy())
      for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]
        permutationHelper(start+1)
        nums[start], nums[i] = nums[i], nums[start]

    permutationHelper(0)
    return ret


a = [1, 2, 3]
print(Solution().permutation(a))
