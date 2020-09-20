class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        
        tmp = []
        for i in s:
            if not i in tmp:
                tmp.append(i)
            else:
                result.append(tmp)
                tmp = []
                tmp.append(i)
                
        result.append(tmp)
        
        result.sort(key=lambda x: len(x))
        print(len(result[-1]))
    
    
if __name__ == '__main__':
    #ll = 'abcabcbb'
    ll = 'dvdf'
    Solution().lengthOfLongestSubstring(ll)
    