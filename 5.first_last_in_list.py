import time


class Solution:
  def firstLastInList(self, nums, target):
    first = self.binarySearch2(nums, 0, len(nums) - 1, target, True)
    last = self.binarySearch2(nums, 0, len(nums)-1, target, False)
    return [first, last]

  def binarySearch(self, nums, low, high, target, isFirst):
    index = None
    while low < high:
      midIndex = (high + low) // 2
      if(target == nums[midIndex]):
        if isFirst:
          index = midIndex
          high = midIndex - 1
        else:
          index = midIndex
          low = midIndex + 1
      elif target > nums[midIndex]:
        low = midIndex + 1
      else:
        high = midIndex - 1
    return index

  def binarySearchRe(self, nums, low, high, target, isFirst):
    if low > high:
      return -1
    midIndex = (high + low) // 2
    if(isFirst):
      if(midIndex == 0 or nums[midIndex] == target and nums[midIndex] > nums[midIndex - 1]):
        return midIndex
      if target > nums[midIndex]:
        return self.binarySearch(nums, midIndex + 1, high, target, isFirst)
      else:
        return self.binarySearch(nums, low, midIndex - 1, target, isFirst)
    else:
      if(midIndex == len(nums) - 1 or nums[midIndex] == target and target < nums[midIndex+1]):
        return midIndex
      elif target < nums[midIndex]:
        return self.binarySearch(nums, low, midIndex - 1, target, False)
      else:
        return self.binarySearch(nums, midIndex + 1, high, target, False)

  def binarySearch2(self, nums, low, high, target, isFirst):
    while True:
      if high < low:
        return -1
      midIndex = (high + low) // 2
      if isFirst:
        if(midIndex == 0 or nums[midIndex] == target and nums[midIndex] > nums[midIndex - 1]):
          return midIndex
        if target > nums[midIndex]:
          low = midIndex + 1
        else:
          high = midIndex - 1
      else:
        if(midIndex == len(nums) - 1 or nums[midIndex] == target and target < nums[midIndex+1]):
          return midIndex
        elif target < nums[midIndex]:
          high = midIndex - 1
        else:
          low = midIndex + 1


#  a sorted list
a = [1, 2, 3, 5, 7, 9, 18]
print(Solution().firstLastInList(a, 7))
