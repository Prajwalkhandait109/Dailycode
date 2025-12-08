'''
Chunky gets happy by eating Melody. Given an array arr[], each element represents the happiness Chunky gets by eating the melody.
Chunky knows why Melody is so chocolaty but will only tell you once you tell him the maximum happiness he can get by eating two adjacent melodies.

Examples:

Input : arr[] = [1, 2, 3, 4, 5]
Output : 9
Explanation: maximum happiness he can get is 9, selecting arr[3] = 4 and arr[4] = 5 which adds up to 9.
Input : arr[] = [2, 1, 3, 4]
Output : 7
Explanation: maximum happiness he can get is 7, selecting arr[2] = 3 and arr[3] = 4 which adds up to 7.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1)

Constraints:
2 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 105
Docstring for .py
'''
#Solution :
class Solution:
    def max_happiness(self, arr):
        max_hap = float('-inf')
        for i in range(len(arr) - 1):
            current = arr[i] + arr[i + 1]
            if current > max_hap:
                max_hap = current
        return max_hap
