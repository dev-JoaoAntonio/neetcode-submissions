class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for y in nums:
            if y in seen:
                return True
            seen.add(y)
        return False