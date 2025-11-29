'''
You are given an array arr and an integer k. In one operation you can choose any element of array and decrease its value by k. You need find the minimum number of operation such that all the elements in the array becomes less or equal to k.

Examples:

Input: arr[] = [5, 3, 2, 6, 8] and k = 5
Output: 2
Explanation: Ishaan can climb a wall with height atmost 5. So he climbs the first 3 walls easily. Now he has to use his power to reduce the height of the 4th wall. After using his power, Now to climb the last wall, he again uses his power.
Input: arr[] = [2, 6, 4, 8, 1, 6] and k = 4 
Output: 3 
Explanation: Ishaan can climb a wall with height atmost 5. He can't climb the wall with height 6, 8, 6.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).
'''
#Solution 1:
#User function Template for python3
import math
class Solution:
    def reducingWalls(self, arr, k):
        #code
        n = len(arr)
        count = 0
        for i in range(n):
            if arr[i] > k:
                if arr[i] > 2*k:
                    count += math.ceil((arr[i] - k) / k)
                else:
                    count += 1
        return count
                
#Solution 2:
#User function Template for python3
class Solution:
    def reducingWalls(self, arr, k):
        n = len(arr)
        count = 0
        for x in arr:
            if x > k:
                # number of operations to make x <= k
                count += (x - k + k - 1) // k
        return count