'''
Given an array arr[]. Your task is to find the minimum and maximum elements in the array.

Examples:

Input: arr[] = [1, 4, 3, -5, -4, 8, 6]
Output: [-5, 8]
Explanation: minimum and maximum elements of array are -5 and 8.
Input: arr[] = [12, 3, 15, 7, 9]
Output: [3, 15]
Explanation: minimum and maximum element of array are 3 and 15.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 109
'''

#Solution 1 :

class Solution:
    def getMinMax(self, arr):
        # code here
        
        minimum = min(arr)
        maximum = max(arr)
        return minimum,maximum
    
    
#Solution 2 :

class Solution:
    def getMinMax(self, arr):
        # code here
        
        a = len(arr)
        minimum = arr.sort()
        maximum = arr[a-1]
        return arr[0],maximum