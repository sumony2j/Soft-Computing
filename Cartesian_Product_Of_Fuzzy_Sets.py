import numpy as np

def cartesian_product_of_two_sets(A,B):
    val=[]
    for i in range(0,len(A)):
        for j in range(0,len(B)):
            if A[i]<B[j]:
                val.append(A[i])
            else:
                val.append(B[j])
    mat=np.array(val).reshape(len(A),len(B))
    return mat

def print_fuzzy_set(A,W):
    for i in range(0,len(A)-1):
        print(f'{round(A[i],2)}/{round(W[i],1)}',end=' + ')
    print(f'{round(A[-1],2)}/{round(W[-1],1)}')

A=list(map(float,input('Enter the values of first fuzzy set : ').strip().split()))
B=list(map(float,input('Enter the values of second fuzzy set : ').strip().split()))
W1=list(map(float,input('Enter the weights of each element for the first fuzzy set : ').strip().split()))
W2=list(map(float,input('Enter the weights of each element for the second fuzzy set : ').strip().split()))

print('The first fuzzy set is :')
print_fuzzy_set(A,W1)
print('The second fuzzy set is :')
print_fuzzy_set(B,W2)

print('The cartesian product of first and second fuzzy set is : \n')
R=cartesian_product_of_two_sets(A,B)
print(f'____|_____{W2[0]}______',end='|')
for i in range(1,len(W2)-1):
    print(f'_____{W2[i]}______',end='|')
print(f'_____{W2[-1]}_____')

for i in range(0,R.shape[0]-1):
    print(f'{W1[i]}  ',end='|')
    for j in range(0,R.shape[1]):
        print(f'____{R[i][j]}_____',end='|')
    print('\n')

print(f'{W1[-1]} ',end='|')
for i in range(0,R.shape[1]):
    print(f'_____{R[-1][i]}____',end='|')
print('\n')
