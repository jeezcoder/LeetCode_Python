class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ret = []
        for elem in A:
            if elem % 2 == 0:
                ret.insert(0, elem)
            else:
                ret.append(elem)
        return ret

if __name__ == "__main__":
    s = Solution()
    A = [3,1,2,4]
    print(s.sortArrayByParity(A))

