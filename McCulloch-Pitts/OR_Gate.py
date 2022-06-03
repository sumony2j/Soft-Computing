# Using MP algo implement OR gate

import sys

x1=int(input('Input The First Value :'))
x2=int(input('Input The Second Value :'))
if x1 not in [0,1]:
    sys.exit('Wrong input ,it should be 1/0')
if x2 not in [0,1]:
    sys.exit('Wrong input ,it should be 1/0')

w1=1
w2=1
b=-1

t=w1*x1+w2*x2+b
print(t)

tr_val=0 # Threshold value

if t>=tr_val:
    print('output =1')
else:
    print('output =0')

