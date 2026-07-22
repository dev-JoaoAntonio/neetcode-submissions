class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}                  
        for i in range(len(nums)):   
            falta = target - nums[i]  
            if falta in vistos:      
                return [vistos[falta], i]
            vistos[nums[i]] = i      