'''
Given two arrays arr1[] and arr2[] of the same size, find the minimum sum of two elements such that one element is from arr1[] and the other is from arr2[], and they are not at the same index in their respective arrays.

Examples:

Input: arr1[] = [5, 4, 13, 2, 1], arr2[] = [2, 3, 4, 6, 5]
Output: 3
Explanation: The minimum sum is obtained by taking 1 from arr1[] and 2 from arr2[]. The sum is 1 + 2 = 3.
Input: arr1[] = [5, 4, 13, 1], arr2[] = [3, 2, 6, 1]
Output: 3
Explanation: The minimum sum is obtained by taking 1 from arr1[] and 2 from arr2[]. We can't take 1 from arr2[] as it is at the same index.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
2 ≤ arr1.size() = arr2.size() ≤ 106
1 ≤ arr1[i], arr2[i] ≤ 105
'''
#Solution :
class Solution:
    def minSum(self, arr1, arr2):
        # Find smallest and second smallest in arr1
        min1_val, min1_idx = float('inf'), -1
        min2_val = float('inf')
        for i, val in enumerate(arr1):
            if val < min1_val:
                min2_val = min1_val
                min1_val = val
                min1_idx = i
            elif val < min2_val:
                min2_val = val

        # Find smallest and second smallest in arr2
        min3_val, min3_idx = float('inf'), -1
        min4_val = float('inf')
        for i, val in enumerate(arr2):
            if val < min3_val:
                min4_val = min3_val
                min3_val = val
                min3_idx = i
            elif val < min4_val:
                min4_val = val

        # If indices of smallest elements are different, return sum directly
        if min1_idx != min3_idx:
            return min1_val + min3_val
        else:
            # Else, take minimum of cross pairs
            return min(min1_val + min4_val, min2_val + min3_val)
