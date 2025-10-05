'''Given a string s, you need to reverse it.

Examples:

Input: s = "Hello"
Output: "olleH"
Explanation: Reverse of Hello is olleH
Input: s = "World"
Output: "dlroW"
Explanation: Reverse of World is dlroW '''

#Solution 1:

def reverseString(s):
    #Index Slicing
    rev = s[::-1]
    return rev


#Solution 2:

def reverseString(s):
    #Using function
    rev ="".join(reversed(s))
    return rev

#Solution 3:

def reverseString(s):
    #Using function
    result=""
    for char in s:
        result= char + result

    return result