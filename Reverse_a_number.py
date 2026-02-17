# reverse a number
# Complete the function below to reverse the digits of given n
def reverseNumber(n):
    # Your code here
    revNum = 0
    while (n > 0):
        lastdigit = n % 10
        n = n // 10
        revNum = (revNum * 10) + lastdigit
    return revNum
        

def main():
    # Test Case 1: Basic positive
    print(reverseNumber(123))  # Expected: 321
    
    # Test Case 2: Single digit
    print(reverseNumber(5))    # Expected: 5
    
    # Test Case 3: With trailing zero
    print(reverseNumber(120))  # Expected: 21
    
    # Test Case 4: Palindrome
    print(reverseNumber(121))  # Expected: 121
    
    # Test Case 5: Larger number
    print(reverseNumber(12345)) # Expected: 54321
    
    # Test Case 6: Zero
    print(reverseNumber(0))    # Expected: 0

if __name__ == "__main__":
    main()
