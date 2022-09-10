class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flag = False
        for item in nums:
            if nums.count(item) > 1:
                flag = True
                break
        return flag
 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_of_nums = set(nums)
        return len(set_of_nums) != len(nums)
 
