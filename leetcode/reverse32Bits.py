class Solution:
    # @param s, a string
    # @return a list of strings
    
    def findRepeatedDnaSequences(self, s):
        hashmap = {}
        lists = []
        for i in range(0,len(s)-9):
            substr = s[0+i:10+i]
            try:
                hashmap[substr] +=1
            except Exception,e:
                hashmap[substr] = 1
        for (k,v) in hashmap.iteritems():
            if(v>1):
                lists.append( k)
        return lists
        
        

print Solution().findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
