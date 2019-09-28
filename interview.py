
val1 = int(input("Number:"))



def rev(val1):
    num = 0
    while(val1>0):
        r = val1%10
        val1=val1//10
        num *=10
        num +=r
    return num
        
if (val1<0):
    print(rev(abs(val1))*-1)
else:            
    print(rev(val1))


#val1 = abs(val1)
#num = rev(val1)
#print(num*-1)
#num = rev(val1)

'''
    
list1 = [[1,2,3],[3,4,5],[6,7,8]]
list2 = [[5,9,8],[1,5,6],[3,2,1]]
list3= [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):#0, 1
    for j in range(3):#0
        if i == j:
            list3[i][j] = list1[i][j]*list2[i][j]
        elif i <j:
            list3[i][j] = list1[i][j]+list2[i][j]
        elif i>j:
            list3[i][j] = list1[i][j]-list2[i][j]
print(list3)
    
'''
