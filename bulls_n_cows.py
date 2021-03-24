class Solution:
    def getHint(self, secret,guess):
        sec_len=len(str(secret))
        guess_len=len(str(guess))
        work_len=max([sec_len,guess_len])
        bulls =  0
        cows = 0
        secret = list(str(secret).zfill(work_len))
        guess = list(str(guess).zfill(work_len))
        for i,j in enumerate(guess):
            if i < len(secret) and j == secret[i]:
                bulls += 1
                secret[i] = '#'
                guess[i] = '$'

        for i,j, in enumerate(guess):
            if j in secret:
                secret.remove(j)
                cows += 1
        

        
       
        return'{0}A{1}B'.format(bulls,cows)




test = Solution()

print(test.getHint(1122,1222))


