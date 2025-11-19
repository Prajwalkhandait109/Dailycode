'''
Given an array arr, the task is to find the maximum triplet sum in the array.

Examples:

Input : arr[] = [4, 2, 7, 9]
Output : 20
Explanation: Here are total 4 combination: (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3).
So, the Sum of these combinations is 13, 15, 20, and 18. The maximum sum is 20.
Input : arr[] = [1, 0, 8, 6, 4, 2] 
Output : 18 
Explanation: (2, 3, 4), this triplet is going to give us a sum of 18.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
3 ≤ arr.size() ≤ 106
-105 ≤ arr[i] ≤ 105
'''
#Solution :
#User function Template for python3

class Solution:
    def maxTripletSum(self, arr) : 
        #Complete the function
        arr.sort(reverse=True)
        add = 0
        for i in range(3):
            add += arr[i]
        return add

            
