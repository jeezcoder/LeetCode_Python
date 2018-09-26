class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            other = target - num
            for j,num in enumerate(nums[i+1:]):
                if num == other:
                    return [i, j+i+1]   

        return [-1, -1]


class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            other = target - num
            try:
                j = nums[i+1:].index(other)
                return [i, j + i + 1]
            except ValueError:
                pass
            
        return [-1, -1]

if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))

