#User function Template for python3
from collections import defaultdict
class Solution:
    def getPairsCount(self, arr, n, k):
        c = 0
        mp = defaultdict(int)
        for i in range(n):
            rem = k - arr[i]
            c += mp[rem]
            mp[arr[i]] += 1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends