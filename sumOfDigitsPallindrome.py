#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self,N):
        #code here

        sum_of_digits = 0
        str_N = str(N)

        for i in range(len(str_N)):
            sum_of_digits += int(str_N[i])

        str_sum = str(sum_of_digits)
        rev_str_sum = ''.join(reversed(str_sum))

        return 1 if str_sum == rev_str_sum else 0

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends
