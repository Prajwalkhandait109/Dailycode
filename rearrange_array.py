'''
Given an array arr of distinct integers. Rearrange the array in such a way that the first element is the smallest and the second element is the largest, the third element is the second smallest and the fourth element is the second largest, and so on.

Examples:

Input: arr[] = [4, 5, 1, 2, 3]
Output: [1, 5, 2, 4, 3]
Explanation: The minimum element is 1, maximum element is 5, second minimum is 2 and so on, thus the rearranged array is [1, 5, 2, 4, 3]
Input: arr[] = [1, 2, 3, 4]
Output: [1, 4, 2, 3]
Explanation: The minimum element is 1, maximum element is 4, second minimum is 2 and so on, thus the rearranged array is [1, 4, 2, 3]
Expected Time Complexity: O(n*logn)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 106
'''
#Solution:
class Solution:
    def Rearrange(self, arr):
        arr.sort()
        n = len(arr)
        first_half = arr[:n // 2]
        second_half = arr[n // 2:]
        second_half.sort(reverse=True)
        
        result = []
        i = 0
        j = 0
        
        while i < len(first_half) and j < len(second_half):
            result.append(first_half[i])
            result.append(second_half[j])
            i += 1
            j += 1
        
        # If odd length, one element remains in second_half
        while j < len(second_half):
            result.append(second_half[j])
            j += 1
        
        return result

                
                
    