'''
Given an array arr of integers. First sort the array then find whether three numbers are such that the sum of two elements equals the third element.

Example:

Input: arr[] = [1, 2, 3, 4, 5]
Output: true
Explanation: The pair (1, 2) sums to 3.
Input: arr[] = [3, 4, 5]
Output: false
Explanation: No triplets satisfy the condition.
Constraints:
1 <= arr.size() <= 103
0 <= arr[i] <= 105


'''
#Solution :
class Solution:
    def findTriplet(self, arr):
        arr_set = set(arr)  # For O(1) lookup
        n = len(arr)
        arr.sort()
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[i] + arr[j] in arr_set:
                    return True
        return False
    