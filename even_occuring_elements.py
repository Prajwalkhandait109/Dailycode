'''
Given an array arr[] of integers, where most numbers occur an odd number of times, except for a few elements that appear an even number of times. Find and return the elements with even occurrences in the array.
If no such element exists, return -1.
Note: Elements should be returned in order of occurrence.

Examples:

Input: arr[] = [9, 12, 23, 10, 12, 12, 15, 23, 14, 12, 15]
Output: [12, 15, 23]
Explanation: The numbers 12, 15, and 23 each appear an even number of times.
Input: arr[] = [23, 12, 56, 34, 32]
Output: [-1]
Explanation: Every number in the array occurs an odd number of times.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:

1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 105
'''
#Solution :
class Solution:
    def findEvenOccurrences(self, arr):
        freq = {}
        result = []
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            
        for key, count in freq.items():
            if count % 2 == 0:
                result.append(key)
                
        n = len(result)
        if n == 0:
            result.append(-1)
            return result
        else:
            return result
