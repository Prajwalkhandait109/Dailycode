'''
Numbers have a measure of friendliness defined as the absolute difference between them. Given an circular array of integers arr[], calculate the friendliness of the array. Friendliness is the sum of the absolute differences between each element and its closest friend in the array.

Examples:

Input: arr[] = [4, 1, 5]
Output: 8
Explanation: The sum of absolute differences with closest neighbors is |4-1| + |1-5| + |5-4| = 8.
Input: arr[] = [1, 1, 1]
Output: 0
Explanation: All elements are identical, so the sum of differences is zero.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
2 < arr.size() ≤ 106
1 ≤ arr[i] ≤ 105
'''
#Solution :
class Solution:
    def calculateFriendliness(self, arr):
        # code here
        n = len(arr)
        abs_diff = 0
        for i in range(len(arr)-1):
            diff = abs(arr[i] - arr[i+1])
            abs_diff += diff
        abs_diff += abs(arr[n-1] - arr[0])
        return abs_diff
            
