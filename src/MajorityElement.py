class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = {}
        for num in nums:
            if num in tmp:
                tmp[num] += 1
            else:
                tmp[num] = 1
        max_value = -1
        ret = None
        for key, value in tmp.items():
            if value > max_value:
                max_value = value
                ret = key
        return ret




if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(Solution().majorityElement(nums))

