class Solution:
    def sumArray(self, arr):
        new = []
        add = 0
        for i in range(len(arr)):
            add += arr[i]
        for i in arr:
            y = add - i
            new.append(y)
        return new

def main():
    # Example array to test
    arr = [1, 2, 3, 4]
    solution = Solution()
    result = solution.sumArray(arr)
    print("Input array:", arr)
    print("Output array:", result)

if __name__ == "__main__":





