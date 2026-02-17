# Complete the function below to check if given n is an Armstrong number
def isArmstrongNumber(n):
    # Your code here
    if n < 0:
        return False
    if n == 0:
        return True  
    
    dup = n
    # Count digits using temp
    count = 0
    temp = n
    while temp > 0:
        temp = temp // 10
        count += 1
    
    # Calculate sum using another temp
    sum_ = 0
    temp = n
    while temp > 0:
        lastdigit = temp % 10
        sum_ += lastdigit ** count
        temp = temp // 10
    
    return sum_ == dup
def main():
    # Test Case 1: Classic Armstrong (153 = 1³ + 5³ + 3³)
    print(isArmstrongNumber(153))    # Expected: True
    
    # Test Case 2: Another Armstrong (371 = 3³ + 7³ + 1³)
    print(isArmstrongNumber(371))    # Expected: True
    
    # Test Case 3: Not Armstrong
    print(isArmstrongNumber(123))    # Expected: False
    
    # Test Case 4: Single digit (all are Armstrong)
    print(isArmstrongNumber(5))      # Expected: True
    
    # Test Case 5: 4-digit Armstrong (1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴)
    print(isArmstrongNumber(1634))   # Expected: True
    
    # Test Case 6: Zero
    print(isArmstrongNumber(0))      # Expected: True
    
    # Test Case 7: Non-Armstrong with same digits
    print(isArmstrongNumber(154))    # Expected: False

if __name__ == "__main__":
    main()
