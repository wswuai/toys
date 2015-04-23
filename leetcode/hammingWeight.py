class Solution:
    # @param num, a list of integers
    # @return a string
    def sorter(self,num,num2):
        ch1 = repr(num)
        ch2 = repr(num2)
        if((len(ch1) - len(ch2)) > 0):
            ch2 = ch2 + '9'*(len(ch1) - len(ch2))
        if((len(ch2) - len(ch1)) > 0):
            ch1 = ch1 + '9'*(len(ch2) - len(ch1))
        return -cmp(int(ch1),int(ch2))
    def largestNumber(self, num):
        res = ''

        a = sorted(num,self.sorter,reverse = False)
        for i in a:
            res += repr(i)
        return res


Solution().largestNumber([4,53,1,3,5])
