class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            res = nums.pop(-1)
            nums.insert(0, res)
        return nums
      
