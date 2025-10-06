'''

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
class patternPrinter:
    def pattern1(self,n):
        for i in range(n):
            for j in range(n):
                print("*",end = "")
            print()
            
        
def main():
    n = 5  
    printer = patternPrinter()
    printer.pattern1(n)

if __name__ == "__main__":
    main()