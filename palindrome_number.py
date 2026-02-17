# palindrome number
# Complete the function below to check if given n is a palindrome number
def isPalindromeNumber(n):
    # Your code here
    dup = n
    revNum = 0 
    while(n > 0):
        lastdigit = n % 10
        n = n // 10
        revNum = (revNum * 10) + lastdigit
    if (dup == revNum):
        return True
    else:
        return False

def main():
    # Test Case 1: Basic palindrome
    print(isPalindromeNumber(121))    # Expected: True
    
    # Test Case 2: Basic non-palindrome
    print(isPalindromeNumber(123))    # Expected: False
    
    # Test Case 3: Single digit (always palindrome)
    print(isPalindromeNumber(5))      # Expected: True
    
    # Test Case 4: With zeros
    print(isPalindromeNumber(1001))   # Expected: True
    
    # Test Case 5: Zero
    print(isPalindromeNumber(0))      # Expected: True
    
    # Test Case 6: Larger palindrome
    print(isPalindromeNumber(12321))  # Expected: True
    
    # Test Case 7: Even length
    print(isPalindromeNumber(1221))   # Expected: True

if __name__ == "__main__":
    main()
