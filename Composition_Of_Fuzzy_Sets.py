import numpy as np

def min_val(l1,l2):
        if l1>l2:
            return l2
        else:
            return l1

C1= int(input('Enter the column number of first matrix : '))
C2= int(input('Enter the column number of second matrix : '))
R1= int(input('Enter the row number of first matrix : '))
R2= int(input('Enter the row number of second matrix : '))

print("Enter the entries in a single line (separated by space): ")

entries1 = list(map(float, input('Enter the values of first matrix : ').strip().split()))
entries2 = list(map(float, input('Enter the values of second matrix : ').strip().split()))

matrix1 = np.array(entries1).reshape(R1, C1)
matrix2 = np.array(entries2).reshape(R2, C2)

min_max=[]
max_product=[]
for i in range(0,R1):
    for j in range(0,C2):
        A=matrix1[i,:]
        B=matrix2[:,j]
        val_min=[]
        val_product=[]
        for k in range(0,len(A)):
            val_min.append(min_val(A[k],B[k]))
            val_product.append(A[k]*B[k])
        min_max.append(max(val_min))
        max_product.append(max(val_product))



result_max_min=np.array(min_max).reshape(R1, C2)
result_max_product=np.array(max_product).reshape(R1, C2)
print('The First Matrix Is : \n',matrix1)
print('The Second Matrix Is : \n',matrix2)
print('The Max-Min Composition Is :\n',result_max_min)
print('The Max-Product Composition Is :\n',result_max_product)

