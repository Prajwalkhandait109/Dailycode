'''
You are given an integer array arr[]. The task is to find the sum of it.

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.
Input: arr[] = [1, 3, 3]
Output: 7
Explanation: 1 + 3 + 3 = 7.
Constraints:
1 <= arr.size <= 105
1 <= arr[i] <= 104

'''

#Solution : 
#User function Template for python3
class Solution:
	def arraySum(self, arr):
   		# code here
   		add = 0
   		for i in range(len(arr)):
   		    add = add + arr[i]
   		return add
   		    
