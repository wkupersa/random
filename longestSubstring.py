class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        accumulator = 0
        len_s = len(s)
        for index in range(0,len_s):
            char_list = []
            if accumulator < len(s[index:]):
                for right_pointer in range(index,len_s):
                    if s[right_pointer] in char_list:
                        break
                    char_list.append(s[right_pointer])
                    accumulator = max(accumulator,len(char_list))
        return accumulator


test = Solution()
print(test.lengthOfLongestSubstring("abcdefgaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaade"))