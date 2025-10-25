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
    
    '''
    1
    2 3
    4 5 6 
    7 8 9 10
    11 12 13 14 15
    '''
    
    def pattern13(self,n):
        count = 1
        for i in range(n+1):
            for j in range(i):
                print(count,end = " ")
                count+=1
            print()
    
    '''
    A
    A B
    A B C
    A B C D
    A B C D E
    ''' 
    def pattern14(self,n):
        for i in range(1, n + 1):
            for j in range(i):
                print(chr(65 + j), end=" ")
            print()
            
            
    '''
    A B C D E
    A B C D
    A B C
    A B
    A
    '''
    def pattern15(self,n):
        for i in range(n,0,-1):
            for j in range(i):
                print(chr(65 + j),end = " ")
            print()
            
            
    '''
    A
    B B
    C C C
    D D D D
    E E E E E
    '''
    def pattern16(self,n):
        for i in range (n):
            for j in range(i+1):
                print(chr(65+i),end = " ")
            print()
            
            
    '''
       A
      ABA
     ABCBA
    ABCDCBA
    '''
    def pattern17(self,n):
        for i in range(n):
            for j in range(n-i):
                print(" ",end = " ")
            for k in range(i+1):
                print(chr(65+k),end = " ")
            for k in range(i-1,-1,-1):
                print(chr(65+k),end = " ")
            for l in range(n-i):
                print(" ",end = " ")
            print()
    '''
    E
    D E
    C D E
    B C D E
    A B C D E
    '''
    def pattern18(self,n):
        for i in range(n):
            for j in range(i,-1,-1):
                print(chr((65+(n-1))-j),end = " ")
            print()
    
    '''
    **********
    ****  ****
    ***    ***
    **      **
    *        *
    *        *
    **      **
    ***    ***
    ****  ****
    **********
    
    '''
    def pattern19(self,n):
        for i in range(n):
            for j in range(n-i):
                print("*",end = " ")
            for k in range(2*i):
                print(" ",end = " ")
            for l in range(n-i):
                print("*",end = " ")
            print()
        for i in range(n-1,-1,-1):
            for j in range(n-i):
                print("*",end = " ")
            for k in range(2*i):
                print(" ",end = " ")
            for l in range(n-i):
                print("*",end = " ")
            print()
            
            
    '''
    *      *
    **    **
    ***  ***
    ********
    ***  ***
    **    **
    *      *
    '''
    def pattern20(self,n):
        for i in range(n):
            for j in range(i+1):
                print("*",end = "")
            for k in range(2*(n-i)-2):
                print(" ", end = "")
            for j in range(i+1):
                print("*",end = "")
            print()
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                print("*",end = "")
            for k in range(2*(n-i)-2):
                print(" ", end = "")
            for j in range(i+1):
                print("*",end = "")
            print()
            
    '''
    * * * *
    *     *
    *     *
    * * * * 
    '''  
    def pattern21(self,n):
        for i in range(n):
             print("*",end = " ")
             if i == 0 or i == n-1:
                for  j in range(n-1):
                    print('*',end = " ")
             elif i!=0 and i!=1 or i!=n-1:
                
                for k in range(2,n):
                    print(" ", end = " ") 
                for l in range(1):
                    print("*",end="")  
                
             print()
             
             
             #OR OPTIMAL
    def pattern22(self,n):
        for i in range(n):
            for j in range(n):
                if i == 0 or i == n-1 or j == 0 or j == n-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

            
            
    '''
    4 4 4 4 4 4 4
    4 3 3 3 3 3 4
    4 3 2 2 2 3 4
    4 3 2 1 2 3 4
    4 3 2 2 2 3 4          
    4 3 3 3 3 3 4     
    4 4 4 4 4 4 4
    '''        
    def pattern23(self,n):
        size = 2 * n - 1
        for i in range(size):
            for j in range (size):
                min_dist=min(i,j,size - i - 1,size - j - 1)
                print(n-min_dist, end = " ")
            print()
            
    '''
    *
    * *
    *   *
    *     *
    * * * * *
    '''
    def pattern24(self,n):
        for i in range(n):
            for j in range(i+1):
                if j==0 or j==i or i==n-1:
                    print("*",end = " ")
                else:
                    print(" ", end  = " ")
                              
                    
            print()
            
    '''
              *
            *   *
          *       *
        *           *
      *               *
    * * * * * * * * * * *
    '''
    def pattern25(self,n):
        
        for i in range(n):
            # Print leading spaces for triangle alignment
            print(" " * (n - i - 1), end="")
            for j in range(2 * i + 1):
                # Outline logic:
                # First row, last row, or first/last star in each row
                if i == n - 1 or j == 0 or j == 2 * i:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
            
            
    '''
    
            *
          * * 
        *   *
      *     *
    * * * * * 
    '''

    def pattern26(self,n):
        for i in range(n):
            # Leading spaces for mirror effect
            print(" " * (n - i - 1) * 2, end="")
            for j in range(i + 1):
                # Outline: left edge (j==0), right edge (j==i), base (i==n-1)
                if j == 0 or j == i or i == n - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

        
    '''
    * * * * *
    *     *
    *   *
    * *
    *
    '''
    def pattern27(self,n):
        for i in range(n,-1,-1):
            for j in range(i+1):
                if j==i or j==0 or i==n:
                    print("*", end = " ")
                else:
                    print(" ",end = " ")
            print()
    
    
def main():
    n = 5
    printer = patternPrinter()
    printer.pattern27(n)

if __name__ == "__main__":
    main()