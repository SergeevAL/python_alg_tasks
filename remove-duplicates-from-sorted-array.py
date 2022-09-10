class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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
