def MIN(x,y):
    r=[]
    for i in range(0,len(x)):
        if x[i]>y[i]:
            r.append(y[i])
        else:
            r.append(x[i])
    return r

def MAX(x,y):
    r=[]
    for i in range(0,len(x)):
        if x[i]<y[i]:
            r.append(y[i])
        else:
            r.append(x[i])
    return r 

A=list(map(float,input('Enter the values of first interval : ').strip().split()))
B=list(map(float,input('Enter the values of second interval : ').strip().split()))

for i in range(len(A)):
    R_in=MIN(A,B)
    R_out=MAX(A,B)
print('The Inner Product is : ',max(R_in))
print('The Outer Product is : ',min(R_out))
