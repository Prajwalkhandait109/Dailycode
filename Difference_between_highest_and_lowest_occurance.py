'''
Given an array, the task is to find the difference between the highest occurrence and lowest occurrence of any number in an array.
Note: If only one type of element is present in the array return 0

Examples:

Input: arr[] = [1, 2, 2]
Output: 1
Explanation:  Lowest occurring element (1) occurs once. Highest occurring element (2) occurs 2 times
Input: arr[] = [7, 8, 4, 5, 4, 1, 1, 7, 7, 2, 5]
Output: 2
Explanation : Lowest occurring element (2) occurs once. Highest occurring element (7) occurs 3 times
Constraints:
1<= arr.size() <=106
1<= arr[i] <=106
'''

#Solution 1 :
#User function Template for python3

class Solution:
    def findDiff(self, arr):
        # code here
        freq = {}
        
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        if len(freq) == 1:
            return 0
            
        max_count = max(freq.values())
        min_count = min(freq.values())
        return max_count - min_count
    
    
#Solution 2 :
from collections import Counter
class Solution:
    def findDiff(self, arr):
        #code here
        freq = Counter(arr)
        if len(freq) == 1:
            return 0
        max_count = max(freq.values())
        min_count = min(freq.values())
        return max_count - min_count