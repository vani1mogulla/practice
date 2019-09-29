import math
for row in range(4):
    for col in range(5):
        if((row == 0 and col%2 != 0) or (row == 1 and col%2 == 0) or (row - col == 1) or (row+col == 5)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    

#Heart Symbol
n = int(input("Enter any number to print heart : "))

if (n%2!=0):n+=1
for i in range(n):
    for j in range(n+1):
        if ((i==0 and j%int(n/2) !=0) or (i == 1 and j%(n//2)==0) or (i-j == n//2-1) or (i+j == n+2) ):
            print("*", end = "")
        else: print(" ", end="")
    print()
print("*"*50)

# M symbol
n=int(input("Enter any number to print M: "))
if(n%2==0):n+=1
for row in range(n):
    for col in range(n):
        if((col==0)or (col==n-1) or(row==col and(row>0 and col<int(n/2)+1)) or((row+col == n-1) and (row<int(n/2)+1))):
            print("*",end="")
        else:print(" ",end="")
    print()
    
#print given string in reverse triangle
string = "Hellovani"
for x in range(len(string)):
    print(string[0:x+1])

num = 9
for i in range(num):
    for j in range(1, num-i+1):
        print(end=" ")
    for k in range(i,0,-1):
        print(k,end="")
    for l in range(2,i+1):
        print(l,end="")
    print()
    
num1 = (num-1)/2 
for r in range(num):
    for c in range(num):
        if((r+c == num1) or (c-r == num1) or (r-c==num1) or (r+c==num1+num-1)):
            print("*",end ="")
        else:print(" ", end="")
    print()

#trianlge of numbers 
inp = int(input("Enter no to print number triangle: "))

for i in range(inp):
    print(" "*(inp-i-1),"* "*(i+1))
for j in range(inp-1,0,-1):
    print(" "*(inp-1-j)," *"*(j))

for i in range(inp):
    print(" "*(inp-i-1),"%s " %(str(i+1))*(i+1))

#Another triangle of numbers
for i in range(inp):
    for j in range(i):
        print(j+1, end = "")
    print()

for i in range(inp,0,-1):
    print(str(i)*i)

#print 'll' in the string
string = "Hello Bella and Llimba Mogulla..."
lst = []
for index, item in enumerate(string):
    if (string[index:index+2]) == 'll':
        lst.append(index)

print(lst, len(string))

#print reverse of a number    
n = int(input("Enter a number to reverse: "))

def rev(n):
    num = 0
    while n>0:
        r = n%10
        n = n // 10
        num = num*10+r
    return num


if (n<0):
    #n = abs(n)
    print(rev(n*-1)*-1)
else:
    print(rev(n))

# print reverse hollow triangle
n = 6

for row in range(n):
    for col in range(n):
        if((row==0 or col==n-1) or (row==col) ):
            print("*", end="")
        else: print(" ", end="")
    print()
