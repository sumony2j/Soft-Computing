
def union(A,B):
    R=[]
    for i in range(0,len(A)):
        if(A[i]>B[i]):
            R.append(A[i])
        else:
            R.append(B[i])
    return R

def intersect(A,B):
    R=[]
    for i in range(0,len(A)):
        if(A[i]<B[i]):
            R.append(A[i])
        else:
            R.append(B[i])
    return R

def complement(A):
    R=[]
    for i in range(0,len(A)):
        V=1-A[i]
        R.append(V)
    return R

def diff(A,B):
    COM_B=complement(B)
    R=[]
    for i in range(0,len(A)):
        if(A[i]<COM_B[i]):
            R.append(A[i])
        else:
            R.append(COM_B[i])
    return R 

def print_fuzzy_set(A,W):
    for i in range(0,len(A)-1):
        print(f'{round(A[i],2)}/{round(W[i],1)}',end=' + ')
    print(f'{round(A[-1],2)}/{round(W[-1],1)}')


A=list(map(float,input('Enter the values of first fuzzy set : ').strip().split()))
B=list(map(float,input('Enter the values of second fuzzy set : ').strip().split()))
W=list(map(int,input('Enter the weights of each element for the fuzzy set : ').strip().split()))
OP=float(input('1.Union\n2.Intersection\n3.Complement\n4.Difference\nEnter the operation which need to be performed from above:'))

print('The first fuzzy set is :')
print_fuzzy_set(A,W)
print('The second fuzzy set is :')
print_fuzzy_set(B,W)

if (OP==1):
    R=union(A,B)
    print('The union of first and second set is :')
    print_fuzzy_set(R,W)
elif (OP==2):
    R=intersect(A,B)
    print('The intersect of first and second set is :')
    print_fuzzy_set(R,W)
elif (OP==3):
    R=complement(A)
    print('The complement of first fuzzy set is :')
    print_fuzzy_set(R,W)
    R=complement(B)
    print('The complement of second fuzzy set is :')
    print_fuzzy_set(R,W)
elif (OP==4):
    R=diff(A,B)
    print('The differnce of first and second set is :')
    print_fuzzy_set(R,W)
else:
    print('Please select any valid number : 1,2,3,4')
    exit()