
def calculate(l,e):
    total=sum(l)
    u_l=[]
    for i in l:
        n_w=i-(e*(total-i))
        if n_w < 0:
            n_w=0
        u_l.append(n_w)
    return u_l

def check_active(l):
    p=0
    loc=0
    n=0
    for i in range(len(l)):
        if l[i] > 0:
            p=p+1
            loc=i+1
        else:
            n=n+1
    if (p==1):
        return loc
    else:
        return 0

w = list(map(float,input('Enter the initial values of activations one by one separated by space :').strip().split()))
n=len(w)
tmp_e=1/n
e=float(input('Input the epsilon value (Skip it if no epsilon is given) : ') or tmp_e)
k=0
print(f'Initial values of activations : {w}')
while(1):
    w=calculate(w,e)
    k=k+1
    print(f'Iteration {k} : {w}')
    c=check_active(w)
    if(c):
        print('Winning neuron is : '+str(c))
        break


