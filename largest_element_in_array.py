'''
Given an array arr[]. The task is to find the largest element and return it.

Examples:

Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.
Input: arr[] = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.
Input: arr[] = [10]
Output: 10
Explanation: There is only one element which is the largest.
Constraints:
1 <= arr.size()<= 106
0 <= arr[i] <= 106

'''

#Solution 1 :

class Solution:
    def largest(self, arr):
        # code here
        if len(arr)==1:
            return arr[0]
        
        largest=arr[0]
        for i in arr:
           if i>largest:
               largest=i
        return largest
        
#Solution 2 :

class Solution:
    def largest(self, arr):
        return max(arr)