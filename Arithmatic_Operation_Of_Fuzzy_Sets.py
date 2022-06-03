from email.mime.base import MIMEBase


def ADD(x,y):
    r=[]
    r.append(x[0]+y[0])
    r.append(x[1]+y[1])
    return r

def SUB(x,y):
    r=[]
    r.append(x[0]-y[1])
    r.append(x[1]-y[0])
    return r

def MUL(x,y):
    r=[]
    r.append(x[0]*y[0])
    r.append(x[1]*y[1])
    return r

def DIV(x,y):
    r=[]
    r.append(x[0]/y[1])
    r.append(x[1]/y[0])
    return r

def IMG(x):
    r=[]
    r.append(-x[1])
    r.append(-x[0])
    return r

def INV(x):
    r=[]
    r.append(1/x[0])
    r.append(1/x[1])
    return r

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


OP=float(input('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Image\n6.Inverse\n7.Minimum\n8.Maximum\nEnter the operation which need to be performed from above:'))


if (OP==1):
    A=list(map(float,input('Enter the values of first interval : ').strip().split()))
    B=list(map(float,input('Enter the values of second interval : ').strip().split()))
    R=ADD(A,B)
    print('The addition of first and second interval is :')
    print(R)
elif (OP==2):
    A=list(map(float,input('Enter the values of first interval : ').strip().split()))
    B=list(map(float,input('Enter the values of second interval : ').strip().split()))
    R=SUB(A,B)
    print('The subtraction of first and second interval is :')
    print(R)
elif (OP==3):
    A=list(map(float,input('Enter the values of first interval : ').strip().split()))
    B=list(map(float,input('Enter the values of second interval : ').strip().split()))
    R=MUL(A,B)
    print('The multiplication of first and second interval is :')
    print(R)
elif (OP==4):
    A=list(map(float,input('Enter the values of first interval : ').strip().split()))
    B=list(map(float,input('Enter the values of second interval : ').strip().split()))
    R=DIV(A,B)
    print('The division of first and second interval is :')
    print(R)
elif (OP==5):
    A=list(map(float,input('Enter the values of the interval : ').strip().split()))
    R=IMG(A)
    print('The image of the interval is :')
    print(R)
elif (OP==6):
    A=list(map(float,input('Enter the values of the interval : ').strip().split()))
    R=INV(A)
    print('The inverse of the interval is :')
    print(R)
elif (OP==7):
    A=list(map(float,input('Enter the values of first interval : ').strip().split()))
    B=list(map(float,input('Enter the values of second interval : ').strip().split()))
    R=MIN(A,B)
    print('The minimam of first and second interval is :')
    print(R)
elif (OP==8):
    A=list(map(float,input('Enter the values of first interval : ').strip().split()))
    B=list(map(float,input('Enter the values of second interval : ').strip().split()))
    R=MAX(A,B)
    print('The maximum of first and second interval is :')
    print(R)
else:
    print('Please select any valid number : 1,2,3,4')
    exit()