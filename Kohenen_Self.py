
def distance(W,X):
    D=0
    for i in range(0,len(W)):
        D=D+pow((W[i]-X[i]),2)
    D=round(D,2)
    return D

def update_weight(W,R,X):
    U_W=[]
    for i in range(0,len(W)):
        U_W.append(W[i]+(R*(X[i]-W[i])))
    return U_W

def print_weight(W,w_n):
    for i in range(0,w_n):
        print(f'W[{i}]={W[i]}')

def print_input(X,v):
    for i in range(0,v):
        print(f'X[{i}]={X[i]}')

W=[]
w_n=int(input('Input the number of weight vectors : '))
for i in range(0,w_n):
    w_i=list(map(float,input(f'Enter the weights of {i} weight vector : ').strip().split()))
    W.append(w_i)

X=[]
v=int(input('Input the number of input vectors : '))
for i in range(0,v):
    x_i=list(map(float,input(f'Enter the inputs of {i} input vector : ').strip().split()))
    X.append(x_i)

L_R=float(input('Enter the learning rate : '))

print('Initial Weights : ')
print_weight(W,w_n)
print('Initial Input Vectors : ')
print_input(X,v)

k=w_n
if (k==len(X[0])):
    p=[]
    for i in range(0,len(W[0])):
        l=[]
        for j in range(0,k):
            l.append(W[j][i])
        p.append(l)
    W=[]
    for i in range(0,len(p)):
        W.append(p[i])
    w_n=len(W)
 
D=[None]*w_n
for j in range(0,v):
    for i in range(0,w_n):
        D[i]=distance(W[i],X[j])
    min_d=D.index(min(D))
    W[min_d]=update_weight(W[min_d],L_R,X[j])

if (k==len(X[0])):
    q=[]
    for i in range(0,len(W[0])):
        l=[]
        for j in range(0,len(W)):
            l.append(W[j][i])
        q.append(l)
    W=[]
    for i in range(0,len(q)):
        W.append(q[i])
    w_n=len(W)

print('Final Weights : ')
print_weight(W,w_n)




