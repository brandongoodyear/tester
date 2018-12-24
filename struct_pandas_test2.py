# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:01:49 2018

@author: Brandon Goodyear
"""

import pandas as pd
import struct 
import numpy as np
import time


starttime=time.time()

x=[i for i in range(50)]
y=[i for i in range(50,len(x)+50)]
t=np.linspace(0,len(x)*0.0000512,num=len(x))

xall=struct.pack('<%ud' %len(x), *x).decode('ISO8859-1')
yall=struct.pack('<%ud' %len(y), *y).decode('ISO8859-1')
tall=struct.pack('<%ud' %len(t), *t).decode('ISO8859-1')

#------------------------------------------------------------------
#getting data in right order with for loop
tiq=[]
for i in range(len(x)):
    tiq.append(t[i])
    tiq.append(x[i])
    tiq.append(y[i])

tiq_s=al=struct.pack('<%ud' %len(tiq), *tiq).decode('ISO8859-1')
#using 8000000 datapoints it only takes about 12 seconds to run all the code, 
#including the for loop 

#try to get tiq list without for loop 


z=pd.DataFrame({'t':t,'i':x,'q':y})
v=z.stack()#makes a list in order time, i, q 
vs=struct.pack('<%ud' %len(v),*v).decode('ISO8859-1')#converts to double precision floating point in 
#the correct order: time, i, q data

endtime=time.time()

print('starttime='+str(starttime)+'\n'+'endtime='+str(endtime)+'\n'+"totaltime="+
      str(endtime-starttime))
print("new clone")
