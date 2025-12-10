'''
The two countries of A and B are at war against each other. The power of these soldiers is given by arr1[i] of A and arr2[i] of B. They can only attack their counterpart enemies like arr1[i] can attack only arr2[i] and not anyone else. Both countries have equal number of counterparts. A soldier with a higher power can kill the enemy soldier. If both soldiers have the same power, they both die. You need to find the winning country.
Note: If no one winning, then return "DRAW".

Examples:

Input: arr1[] = [2, 2], arr2[] = [5, 5]
Output: B
Explanation: Both countries have 2 soldiers. arr2[0] kills arr1[0], arr2[1] kills arr1[1]. A has 0 soldiers alive at the end. B has both soldiers alive at the end.Return "B" as a winner.
Input: arr1[] = [9], arr2[] = [8]  
Output: A
Explanation: arr1[0] > arr2[0], So A is the winner.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ arr1.size() ≤ 106
0 ≤ arr1[i],arr2[i] ≤ 10Docstring for countries_at_war
'''
#Solution :
#User function Template for python3


class Solution:
    def countryAtWar(self, arr1, arr2):
        countA = 0
        countB = 0
        
        for i in range(len(arr1)):
            if arr1[i] > arr2[i]:
                countA += 1
            else:  # arr1[i] < arr2[i]
                countB += 1
                
        if countA == countB:
            return "DRAW"
        elif countA > countB:
            return "A"
        else:
            return "B"

                    
                    
