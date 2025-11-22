'''
Given an array arr of even size, sort the first half of the array in ascending order and the second half in descending order.

Examples :

Input: arr[] = [10, 20, 30, 40]
Output: [10, 20, 40, 30]
Explanation: The 10 and 20 will be sorted in ascending order and 30 and 40 will be sorted in descending order.
Input: arr[] = [5, 4, 6, 2, 3, 8, 9, 7]
Output: [2, 4, 5, 6, 9, 8, 7, 3] 
Explanation: The 5, 4, 6, 2 will be sorted in ascending order and 3, 8, 9, 7 will be sorted in descending order.
Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(1)

Constraints: 
1 <= arr.size() <= 105
1 <= arr[i] <= 10
'''

#Solution :
#User function Template for python3

class Solution:
    def customSort(self, arr):
        # code here
        n = len(arr)
        new = arr[:n//2]
        new.sort()
        second_half = arr[n//2:]
        second_half.sort(reverse = True)
        return new + second_half