'''
Given an array arr of even size consisting of positive integers. After sorting the array, find the sum of the product of i-th element from starting and i-th element from last.

Examples:

Input: arr[] = [9, 2, 8, 4, 5, 7, 6, 0]
Output: 74
Explanation: Required sum can be obtained as 9*0 + 8*2 + 7*4 + 6*5 which is equal to 74.
Input: arr[] = [1, 2, 3, 4]
Output: 10
Explanation: array is already sorted 1*4 + 2*3 = 10
Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(1)

Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 103
'''
#Solution :
#User function Template for python3

class Solution:
    def altProduct(self, arr):
        arr.sort()
        n = len(arr)
        result = 0
        i, j = 0, n - 1

        while i <= j:
            if i == j:
                # If odd length, add the square of the middle element once
                result += arr[i] * arr[j]
            else:
                result += arr[i] * arr[j]
            i += 1
            j -= 1

        return result
