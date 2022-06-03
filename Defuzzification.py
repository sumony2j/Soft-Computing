
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

OP=float(input('1.Union\n2.Intersection\n3.Complement\n4.Difference\n5.Normal-Transformation\nEnter the operation which need to be performed from above:'))

if (OP==1):
    A=list(map(float,input('Enter the values of first fuzzy set : ').strip().split()))
    B=list(map(float,input('Enter the values of second fuzzy set : ').strip().split()))
    W=list(map(int,input('Enter the weights of each element for the fuzzy set : ').strip().split()))
    lam=float(input('Enter the lamdha value : '))
    R=union(A,B)
    R=[x for x in R if x>lam]
    print('The union of first and second set is :')
    print_fuzzy_set(R,W)
elif (OP==2):
    A=list(map(float,input('Enter the values of first fuzzy set : ').strip().split()))
    B=list(map(float,input('Enter the values of second fuzzy set : ').strip().split()))
    W=list(map(int,input('Enter the weights of each element for the fuzzy set : ').strip().split()))
    lam=float(input('Enter the lamdha value : '))
    R=intersect(A,B)
    R=[x for x in R if x>lam]
    print('The intersect of first and second set is :')
    print_fuzzy_set(R,W)
elif (OP==3):
    A=list(map(float,input('Enter the values of fuzzy set : ').strip().split()))
    W=list(map(int,input('Enter the weights of each element for the fuzzy set : ').strip().split()))
    lam=float(input('Enter the lamdha value : '))
    R=complement(A)
    R=[x for x in R if x>lam]
    print('The complement of first fuzzy set is :')
    print_fuzzy_set(R,W)
elif (OP==4):
    A=list(map(float,input('Enter the values of first fuzzy set : ').strip().split()))
    B=list(map(float,input('Enter the values of second fuzzy set : ').strip().split()))
    W=list(map(int,input('Enter the weights of each element for the fuzzy set : ').strip().split()))
    lam=float(input('Enter the lamdha value : '))
    R=diff(A,B)
    R=[x for x in R if x>lam]
    print('The differnce of first and second set is :')
    print_fuzzy_set(R,W)
elif (OP==5):
    A=list(map(float,input('Enter the values of fuzzy set : ').strip().split()))
    W=list(input('Enter the weights of each element for the fuzzy set : ').strip().split())
    lam=float(input('Enter the lamdha value : '))
    R=[x for x in A if x>lam]
    for i in range(0,len(R)-1):
        print(f'{round(R[i],2)}/{W[i]}',end=' + ')
    print(f'{round(R[-1],2)}/{W[-1]}')
else:
    print('Please select any valid number : 1,2,3,4')
    exit()