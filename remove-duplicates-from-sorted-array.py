class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Input: nums = [0,0,1,1,1,2,2,3,3,4]
        # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        # Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
        # It does not matter what you leave beyond the returned k (hence they are underscores).
        # индексы начинаются с нуля
        # current_index который создает новый порядок
        # на return необходимо current_index + 1 так как последнее значение и идущие за ним не изменяться 
        current_index = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[current_index]:
                current_index += 1
                nums[current_index] = nums[i]
        print(nums)
        return current_index + 1
