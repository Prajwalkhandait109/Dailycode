'''
Given an array arr[], print all its elements space-separated.

Note: You don't need to move to the next line after printing all elements of the array (space-separated)

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: 1 2 3 4 5
Input: arr[] = [2, 3, 5, 5]
Output: 2 3 5 5
Constraints:
1 <= arr.size <= 106
1 <= arr[i] <= 108
'''

#Solution :
#User function Template for python3
class Solution:
    
    # Just print the space seperated array elements
	def printArray(self, arr):
	    # code here
	    a = len(arr)
	    for i in range(a):
	        
	        
            print(int(arr[i]), end = " ")