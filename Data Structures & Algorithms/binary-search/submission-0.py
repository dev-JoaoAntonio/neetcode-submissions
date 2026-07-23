class Solution:
    def search(self, nums: List[int], target: int) -> int:
        dic = {}
        for i, n in enumerate(nums):
            dic[n] = i
            if target in dic:
                return i
        return -1