'''
Given two sorted arrays arr1 and arr2 of distinct elements. Given a value x. The problem is to count all pairs from both arrays whose sum equals x.
Note: The pair has an element from each array.

Examples:

Input: x = 10, arr1[] = [1, 3, 5, 7], arr2[] = [2, 3, 5, 8] 
Output: 2
Explanation: The pairs are: (5, 5) and (7, 3).  
Input: x = 5, arr1[] = [1, 2, 3, 4], arr2[] = [5, 6, 7, 8]
Output: 0
Explanation: There are no valid pairs.
Expected Time Complexity: O(n+m).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ x ≤ 109
1 ≤ arr1.size(), arr2.size() ≤ 106
1 ≤ arr1[i], arr2[i] ≤ 106

'''

#Solution :
#User function Template for python3

class Solution:
    def countPairs(self, arr1, arr2, x):
        freq = {}
        for num in arr2:
            freq[num] = freq.get(num, 0) + 1  # Count occurrences
            
        count = 0
        for a in arr1:
            complement = x - a
            count += freq.get(complement, 0)
        return count
