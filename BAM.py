from turtle import shape
import numpy as np

input_number=int(input('Enter the number of inputs : '))
target_number=input_number
input_vector=[]
target_vector=[]
for i in range(input_number):
    input_vector.append(list(map(int,input(f'Enter the elements of Input[{i}] : ').strip().split())))
for i in range(target_number):
    target_vector.append(list(map(int,input(f'Enter the elements of Target[{i}] : ').strip().split())))

r=len(input_vector[0])
c=len(target_vector[0])
W=np.zeros([])
for i in range(input_number):
    input_vector_T=np.array([input_vector[i]]).T
    target_vector_A=np.array([target_vector[i]])
    W=W+np.matmul(input_vector_T,target_vector_A)

print('Final weight for X will be : ')
print(W)
print('Final weight for Y will be : ')
print(W.T)


