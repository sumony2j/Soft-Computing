# Using MP algo implement NOT gate

import sys

x1=int(input('Input The Value :'))
if x1 not in [0,1]:
    sys.exit('Wrong input ,it should be 1/0')

w1=-1

t=w1*x1
print(t)

tr_val=0 # Threshold value

if t>=tr_val:
    print('output =1')
else:
    print('output =0')

