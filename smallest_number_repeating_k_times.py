'''
Given an array arr, the goal is to find out the smallest number that is repeated exactly ‘k’ times.
Note: If there is no such element then return -1.

Example:

Input: arr[] = [2, 2, 1, 3, 1], k = 2
Output: 1
Explanation: Here in array, 2 is repeated 2 times, 1 is repeated 2 times, 3 is repeated 1 time. Hence 2 and 1 both are repeated 'k' times i.e 2 and min(2, 1) is 1 .
Input: arr[] = [3, 5, 3, 2], k = 1
Output:  2 
Explanation: Both 2 and 5 are repeating 1 time but min(5, 2) is 2.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 104


'''
#Solution :
#User function Template for python3

class Solution:
    def findDuplicate(self, arr, k):
        # code here
        freq = {}
        arr.sort()
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        candidate = [num for num , count in freq.items() if count == k]
        
        if candidate:
            return min(candidate)
        else:
            return -1
        