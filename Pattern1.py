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
      
    #Pattern 2     
    '''
    *
    * *
    * * *
    * * * *
    * * * * *

    ''' 
    def pattern2(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*",end = " ") 
            print()    
            
        
    '''
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5

    '''        

    def pattern3(self,n):
        for i in range(n):
            for j in range(i+1):
                print(j+1,end = " ")
            print()
            
    '''
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    
    '''
    def pattern4(self,n):
        for i in range(n):
            for j in range (i+1):
                print(i+1,end = " ")
            print()
            
            
    '''
    * * * * *
    * * * *
    * * *
    * *
    *
    
    '''
    def pattern5(self,n):
        for i in range(n,0,-1):
            for j in range(i):
                print("*",end = " ")
            print()    
    
    '''
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
    
    '''
    def pattern6(self,n):
        for i in range(n,0,-1):
            for j in range(i):
                print(j+1,end = " ")
            print()
            
    '''
        *    
      * * *
    * * * * *
  * * * * * * *
    '''
    def pattern7(self,n):
        for i in range(n):
            for j in range(n-i):
                print(" ",end = " ")
            for k in range(i*2+1):
                print("*",end = " ")
            for l in range(n-i):
                print(" ",end = " ")
            print()
    
    '''
    * * * * * * *
      * * * * *
        * * *
          * 
    '''
    def pattern8(self,n):
        for i in range(n,-1,-1):
            for j in range(n-i):
                print(" ", end = " ")
            for k in range(2*i+1):
                print("*",end = " ")
            for l in range(n-i):
                print(" ",end = " ")
            print()
            
    '''
          *    
        * * *
      * * * * *
    * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          * 
    '''
          
    def pattern9(self,n):
        for i in range(n):
            for j in range(n-i):
                print(" ",end = " ")
            for k in range(2*i+1):
                print("*",end = " ")
            for l in range(n-i):
                print(" ",end = " ")
            print()
        for i in range(n-1,-1,-1):
            for j in range(n-i):
                print(" ", end = " ")
            for k in range(2*i+1):
                print("*",end = " ")
            for l in range(n-i):
                print(" ",end = " ")
            print()
            #OROROROROROROROROROROR
    def patternOR(self, n):
        for i in range(n):
            print('  ' * (n - i) +' *'* (2 * i + 1),end = " ")
            print()
        for i in range(n - 2, -1, -1):
            print('  ' * (n - i) + ' *' * (2 * i + 1), end = " ")
            print()

               
    '''
    *
    * *
    * * *
    * * * *
    * * *
    * *
    *
    
    '''
    def pattern10(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*",end = " ")
            print()          
        for i in range(n-1,0,-1):
            for j in range(i):
                print("*",end = " ")
            print()
            
    '''
    1
    0 1
    1 0 1
    0 1 0 1
    1 0 1 0 1
    
    '''
    def pattern11(self,n):
        for i in range(1,n+1):
            flag = i % 2
            for j in range(i):
                #print((i + j)%2, end = " ")
                print(flag, end=" ")
                flag = 1- flag
            print()    
         
            
    '''
    1      1
    12    21
    123  321
    12344321
    '''     
    def pattern12(self,n):
        for i in range(1,n+1):
            for j in range(i):
                print(j+1,end = "")
            print(" "* (2*(n-i)),end = " ")
            for j in range(i,0,-1):
                print(j,end= "")
                
            print()
    
    
    
      
    
def main():
    n = 5  
    printer = patternPrinter()
    printer.pattern12(n)

if __name__ == "__main__":
    main()