# form given n(number) find the count of digits 
# Complete the function below to count the number of digits in given n
def countDigits(n):
    # Your code here
    if n == 0:
        return 1
    count = 0
    while(n > 0):
        lastdigit = n % 10
        n = n // 10
        count += 1
    return count
    

def main():
    # Test Case 1: Single digit
    print(countDigits(5))  # Expected: 1
    
    # Test Case 2: Multi-digit number
    print(countDigits(123))  # Expected: 3
    
    # Test Case 3: Larger number
    print(countDigits(1000))  # Expected: 4
    
    # Test Case 4: Number with zeros
    print(countDigits(1024))  # Expected: 4
    
    # Test Case 5: Single digit zero
    print(countDigits(0))  # Expected: 1
    
    # Test Case 6: Very large number
    print(countDigits(1234567890))  # Expected: 10

if __name__ == "__main__":
    main()
