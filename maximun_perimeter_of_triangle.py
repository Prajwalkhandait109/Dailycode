'''
Given an array arr[] of positive integers. Find out the maximum perimeter of the triangle from the array.

Examples:

Input: arr[] = [6, 1, 6, 5, 8, 4]
Output: 20
Explanation: Triangle formed by  8,6 & 6. Thus perimeter 20.
Input: arr[] = [7, 55, 20, 1, 4, 33, 12]
Output:  -1
Explanation:As the triangle is not possible because the condition: the sum of two sides should be greater than third is not fulfilled here.
Expected Time Complexity: O(n*logn).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤105
'''
#Solution :
class Solution:
    def maxPerimeter(self, arr):
        n = len(arr)
        # sort in descending order
        arr.sort(reverse=True)

        # check every consecutive triplet
        for i in range(n - 2):
            a, b, c = arr[i], arr[i + 1], arr[i + 2]
            # triangle condition (largest side is a)
            if a < b + c:
                return a + b + c

        # no valid triangle
        return -1