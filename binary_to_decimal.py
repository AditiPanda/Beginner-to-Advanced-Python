#User function Template for python3

class Solution:
    def binary_to_decimal(self, s):
        # Code here
        rev_str = ''.join(reversed(s))
        ans = 0
        for i in range(len(rev_str)):
            ans += int(rev_str[i])*(2**i)
        return ans

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        str = input()
        ob = Solution();
        ans = ob.binary_to_decimal(str)
        print(ans)
# } Driver Code Ends
