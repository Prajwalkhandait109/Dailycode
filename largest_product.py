'''
Given an array arr and an integer k. You have to find the maximum product of k contiguous elements in the array. 

Examples:

Input: arr[] = [1, 2, 3, 4] and k = 2
Output: 12 
Explanation: The sub-array of size 2 will be 3 4 and the product is 12.
Input: arr[] = [1, 6, 7, 8] and k = 3
Output: 336
Explanation: The sub-array of size 3 will be 6 7 8 and the product is 336.
Expected Time Complexity: O(n)
Expected Auxilary Space: O(1)

Constraints:
1 <= arr.size() <= 106
1 <= k<= 8
1<= arr[i] <=102
'''
#Solution :
# You are required to complete this fucntion
# Function should return the an integer
class Solution:
    def findMaxProduct(self, arr, k):
        mod = 10**9 + 7
        n = len(arr)
        
        # Calculate the product of the first window of size k
        prod = 1
        for i in range(k):
            prod *= arr[i]
        max_prod = prod
        
        # Slide the window from index k to end
        for i in range(k, n):
            # To avoid division by zero, handle zeros carefully
            if arr[i - k] != 0:
                prod = prod // arr[i - k] * arr[i]
            else:
                # Recalculate product from scratch if zero was in previous window
                prod = 1
                for j in range(i - k + 1, i + 1):
                    prod *= arr[j]
            
            if prod > max_prod:
                max_prod = prod
                
        return max_prod % mod