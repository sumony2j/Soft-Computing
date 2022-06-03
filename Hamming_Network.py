import numpy as np

input_vector_number=int(input('Enter the number of input vectors : '))
exemplar_vector_number=int(input('Enter the number of exemplar vectors : '))
input_vector=[]
exemplar_vector=[]
exemplar_vector_update=[]
for i in range(input_vector_number):
    input_vector.append(np.array(input(f'Enter the elements of Input[{i}] : ').strip().split(),int))
for i in range(exemplar_vector_number):
    exemplar_vector.append(np.array(input(f'Enter the elements of Exemplar[{i}] : ').strip().split(),int))

B=input_vector_number/2
b=np.array(B)
for i in range(0,exemplar_vector_number):
    exemplar_vector_update.append(exemplar_vector[i]/2)
print('Initial weights are : ')
for i in range(0,exemplar_vector_number):
        print(f'W[{i}]',end='        ')
print('\n')
for j in range(0,len(exemplar_vector[0])):
    for i in range(exemplar_vector_number):
        print(f' {exemplar_vector_update[i][j]}',end='          ')
    print('\n')

for i in range(input_vector_number):
    y=[]
    print(f'For Input vector {i}: ')
    for j in range(exemplar_vector_number):
        k=np.matmul(input_vector[i],exemplar_vector_update[j].T)
        y.append(np.add(k,b))
        print(f'Value of Y[{j}]={y[j]}')
    min_in=y.index(max(y))
    print(f'Y[{min_in}] has the best exemplar for Input vector {i}')



