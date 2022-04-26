#User function Template for python3
from math import floor

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        # code here

        temp = 0
        str_n = str(n)
        for i in range(len(str_n)):
            temp += pow(int(str_n[i]), 3)

        return 'Yes' if n == temp else 'No'

#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends
