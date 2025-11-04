'''
Given an array arr of  positive integers. You need to return the minimum product of k integers of the given array.

Examples:

Input: arr[] = [1, 2, 3, 4, 5], k = 2
Output: 2
Explanation: We will get the minimum product after multiplying 1 and 2 that is 2. So, the answer is 2.
Input: arr[] = [9, 10, 8], k = 3
Output: 720
Explanation: We have to multiply all the numbers.
Constraints:
1 ≤ k, arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
'''
#SOLUTION :
class Solution:
    def minProduct(self, arr, k):
        MOD = 10**9 + 7
        arr.sort()
        if k > len(arr):
            k = len(arr)
        product = 1
        for i in range(k):
            product = (product * arr[i]) % MOD
        return product






