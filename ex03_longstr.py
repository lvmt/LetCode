class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''移动窗口解法
        '''
        if not s:
            return 0
        
        if len(s) == 1:
            return 1
        
        result_set = set()
        max_n = 0
        for i in range(len(s)):
            if s[i] in result_set:
                length = len(result_set)
                max_n = length  if length > max_n else max_n
                result_set.clear()
                result_set.add(s[i])
            else:
                result_set.add(s[i])
        
        length = len(result_set)
        max_n = length  if length > max_n else max_n  
                
        #print(max(record_length))
        return max_n
    
                

if __name__ == '__main__':
    #ll = 'abcabcbb'
    ll = "auxj"
    print(Solution().lengthOfLongestSubstring(ll))
    