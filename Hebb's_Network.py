vector=[]
input_vector=int(input('Enter the Number of inputs : '))
for i in range(input_vector):
    vector.append(list(map(float,input(f'Enter the input-{i} : ').strip().split())))
output=list(map(float,input(f'Enter the output : ').strip().split()))
weight=list(map(float,input(f'Enter the weights : ').strip().split()))
n=float(input('Enter the learning rate : '))
bias=float(input('Enter the bias : '))

for i in range(len(vector[0])):
    for j in range(input_vector):
        weight[j]=weight[j]+n*output[i]*vector[j][i]
    bias=bias+n*output[i]
    print('--------------------')
    print(f'For input-{i} : ')
    print(f'weight : {weight}')
    print(f'bias : {bias}')









