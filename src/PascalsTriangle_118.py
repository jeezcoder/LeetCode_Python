class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []

        ret = [[1]]
        for x in range(1, numRows):
            temp = [1]
            for y in range(1,x):
                temp.append(ret[x-1][y-1] + ret[x-1][y])
            temp.append(1)
            ret.append(temp)
        return ret

if __name__ == "__main__":
    rows = 5
    print(Solution().generate(rows))


