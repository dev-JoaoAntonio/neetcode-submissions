class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer, right_pointer = 0,len(nums)-1
        while left_pointer<=right_pointer:
            midpoint = left_pointer + (right_pointer - left_pointer) // 2
            if nums[midpoint] == target:
                return midpoint
            elif target < nums[midpoint]:
                right_pointer = midpoint - 1
            else:
                left_pointer = midpoint + 1
        return -1