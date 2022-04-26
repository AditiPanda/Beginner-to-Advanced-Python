#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, n, s):
        #Write your code here
        temp = 0
        i = 0
        j = 0

        while (i < n & temp < s):
            temp += arr[j]
            print(temp,i,j)
            if temp < s:
                j += 1
                continue
            if temp > s:
                j += 1
                i = 0
                continue
            if temp == s:
                break
            i +=1

        return j, i
#{
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):

            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])

            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)

            for i in ans:
                print(i, end=" ")

            print()

            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
