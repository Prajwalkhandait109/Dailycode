'''
Check whether given two arrays a[] and b[] are identical or not. Two arrays are called identical arrays if they contain the same element with the same count, regardless of the order of elements.

Examples:

Input: a[] = [1, 2, 3, 4, 5], b[] = [3, 4, 1, 2, 5]
Output: true
Explanation: Here we can see array a[] = [1, 2, 3, 4, 5] and b[] = [3, 4, 1, 2, 5]. If we look both the array then we can get that array b[] is the permutation of a[]. So, both array.are identical. 
Input: a[] = [1, 2, 4], b[] = [3, 2, 1]
Output: false
Explanation: Here we can see that, missing 4 in array b and has 3 so they are not identical.
Constraints:
1 ≤ a.size(), b.size() ≤ 105
a.size() = b.size()
1 ≤ a[i], b[i] ≤ 105'''

#Solution :
#User function Template for python3
# arr1 number[] 
# arr2 number[] 
# return boolean
class Solution:
    def isIdentical(self, a, b):
        #Your code goes here.
        a.sort()
        b.sort()
        if a == b:
            return True
        else:
            return False
        