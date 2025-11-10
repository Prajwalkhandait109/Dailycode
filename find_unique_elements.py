'''
Given an array of elements occurring in multiples of k, except one element which doesn't occur in multiple of k. Return the unique element.

Examples:

Input: k = 3, arr[] = [6, 2, 5, 2, 2, 6, 6]
Output: 5
Explanation: Every element appears 3 times except 5.
Input: k = 4, arr[] = [2, 2, 2, 10, 2]
Output: 10
Explanation: Every element appears 4 times except 10.
Expected Time Complexity: O(n* log(arr[i]))
Expected Auxiliary Space: O(log(arr[i]))

Constraints:
3<= arr.size()<=2*105
2<= k<=2*105
1<= arr[i]<=109
'''
#Solution :

class Solution:
    def find_unique(self, k, arr):
        #code here
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        min_freq = None
        min_num = None
        for num in freq:
            if min_freq is None or freq[num] < min_freq:
                min_freq = freq[num]
                min_num = num
                
        return min_num