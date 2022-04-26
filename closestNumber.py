#User function Template for python3

class Solution:
    def closestNumber(self, N , M):
        # code here
        temp_minus = N
        temp_plus = N

        count_minus = 0
        count_plus = 0

        while(temp_minus %M != 0):
            temp_minus -= 1
            count_minus += 1
        while(temp_plus %M != 0):
            temp_plus += 1
            count_plus += 1

        #ans = temp_minus if count_minus < count_plus else temp_plus
        if count_minus == count_plus:
            return min(temp_minus, temp_plus)

        return temp_minus if count_minus < count_plus else temp_plus

#Another Version
import numpy

class Solution:
    def findDistance(self, N, M, direction):
        remainders = numpy.array([i%M for i in range(abs(N),0,-1)]) if direction == '-' else numpy.array([i%M for i in range(abs(N),abs(N)+M)])
        dist = numpy.where(remainders == 0)[0][0]
        #return N - dist if direction == '-' else N + dist
        return dist

    def closestNumber(self, N , M):
        # code here
        dist_minus = self.findDistance(N, M, '-')
        dist_plus = self.findDistance(N, M, '+')
        return min(N-dist_minus, N+dist_plus)





#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())

        ob = Solution()
        print(ob.closestNumber(N,M))
# } Driver Code Ends
