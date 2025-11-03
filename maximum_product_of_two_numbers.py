'''
Given an array arr of non-negative integers, return the maximum product of two numbers possible.

Example:

Input: arr[] = [1, 4, 3, 6, 7, 0] 
Output: 42
Explanation: 6 and 7 have the maximum product.
Input: arr[] = [1, 100, 42, 4, 23]
Output: 4200
Explanation:  42 and 100 have the maximum product.
Constraints:
2 ≤ arr.size ≤ 107
0 ≤ arr[i] ≤ 109
'''

#Solution :
#User function Template for python3
class Solution:

	def maxProduct(self,arr):
		# code here
		arr.sort()
		new = arr[::-1]
		
	    return new[0] * new[1]