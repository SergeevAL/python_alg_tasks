# Основной подход сравнивать с помощью xor, 0 ^ 0 = 0, 5^5 = 0, x ^ 0 = x

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for item in nums:
            res ^= item
        return res
