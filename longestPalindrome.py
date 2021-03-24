class Solution:
    def longestPalindrome(self, s: str) -> str:
        # how many pairs of letters are there. The max palindrome 
        # Can not be larger than that + 1
        #  Then desend from there
        # determine Window as substring shifts
        # Need to account for odd and even length palindromes
        # First one found should be the answer
        #
        #trivial 
        max_size = self.max_size_of_palindrome(s)
        if max_size == 0:
            return max_size
        print("max_size is {}".format(max_size))
        s_len = len(s)
        for i in range(max_size,1,-1):
            # J is starting position in the string
            # need to look at string windows
            j = 0 
            while (j + i) <= s_len:
                print("max_size is {}".format(i))
                temp_s = s[j:i+j]
                #print("Comparing {}".format(temp_s))
                if self.isPalindrome(temp_s):
                    return temp_s
                j += 1
          


    def max_size_of_palindrome(self, s: str) -> int :
        # determine maximum possible size of palandrome by 
        # looking for number of letter pairs. 
        # we need to add one as there may be a single 
        # character in the middle of the string. 
        char_dict = {}
        for i in s:
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
        register = 0 
        for  i in char_dict.keys():
            register += char_dict[i]//2    
        return 2*register+1


    def isPalindrome(self, s: str):
        s_len = len(s)
        
        # if the string legth is odd,
        # we don't test the middle character
        modulo = s_len%2
        middle  = int(s_len/2) 
        left = s[0:middle]
        right = s[:middle-1 + modulo:-1]
        if left == right:   
            return True
        return False


test = Solution()
#print(test.longestPalindrome("mqizdjrfqtmcsruvvlhdgzfrmxgmmbguroxcbhalzggxhzwfznfkrdwsvzhieqvsrbyedqxwmnvovvnesphgddoikfwuujrhxwcrbttfbmlayrlmpromlzwzrkjkzdvdkpqtbzszrngczvgspzpfnvwuifzjdrmwfadophxscxtbavrhfkadhxrmvlmofbzqshqxazzwjextdpuszwgrxirmmlqitjjpijptmqfbggkwaolpbdglmsvlwdummsrdyjhmgrasrblpjsrpkkgknsucsshjuxunqiouzrdwwooxclutkrujpfebjpoodvhknayilcxjrvnykfjhvsikjabsdnvgguoiyldshbsmsrrlwmkfmyjbbsylhrusubcglaemnurpuvlyyknbqelmkkyamrcmjbncpafchacckhymtasylyfjuribqxsekbjkgzrvzjmjkquxfwopsbjudggnfbuyyfizefgxamocxjgkwxidkgursrcsjwwyeiymoafgyjlhtcdkgrikzzlenqgtdukivvdsalepyvehaklejxxmmoycrtsvzugudwirgywvsxqapxyjedbdhvkkvrxxsgifcldkspgdnjnnzfalaslwqfylmzvbxuscatomnmgarkvuccblpoktlpnazyeazhfucmfpalbujhzbykdgcirnqivdwxnnuznrwdjslwdwgpvjehqcbtjljnxsebtqujhmteknbinrloregnphwhnfidfsqdtaexencwzszlpmxjicoduejjomqzsmrgdgvlrfcrbyfutidkryspmoyzlgfltclmhaeebfbunrwqytzhuxghxkfwtjrfyxavcjwnvbaydjnarrhiyjavlmfsstewtxrcifcllnugldnfyswnsewqwnvbgtatccfeqyjgqbnufwttaokibyrldhoniwqsflvlwnjmffoirzmoxqxunkuepj"))
print(test.longestPalindrome("mqizdjrfqtmcsababbabaruvvlhdgzfrmxgmmbguro"))


