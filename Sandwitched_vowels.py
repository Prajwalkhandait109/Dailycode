'''
For a given string s comprising only lowercase English alphabets, eliminate the vowels from the string that occur between two consonants(sandwiched between two immediately adjacent consonants). Return the new string.

Examples:

Input : s = "bab"
Output : bb
Explanation: 'a' is a vowel occuring between two consonants i.e. b. Hence the updated string eliminates a.
Input : s = "ceghij"
Output : cghj
Explanation: 'e' and 'i' are sandwitched vowels.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ s.size() ≤ 106
'a' ≤ s[i] ≤ 'z'
'''

#Solution :
#User function Template for python3

  
def Sandwiched_Vowel(s):
    #Complete the function
    vowels = set('aeiou')
    n = len(s)
    result = []

    for i in range(n):
        # Check if s[i] is a vowel
        if s[i] in vowels:
            # Check if it has consonants on both sides
            if i > 0 and i < n-1 and s[i-1] not in vowels and s[i+1] not in vowels:
                continue  # Skip this vowel!
        # Add character to result
        result.append(s[i])

    return ''.join(result)