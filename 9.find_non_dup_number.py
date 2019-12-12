class Solution(object):
  def singleNumber(self, nums):
    occurance = {}
    for n in nums:
      occurance[n] = occurance.get(n, 0) + 1

    for key, value in occurance.items():
      if(value == 1):
        return key

  def singleNumber2(self, nums):
    unique = 0
    for n in nums:
      unique ^= n
    return unique
