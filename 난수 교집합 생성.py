import sys
import numpy as np
import pandas as pd
            
a=list(np.random.randint(1,30,10))
b=list(np.random.randint(1,30,10)) 

inter=[]
for i in a:
    if i in b:
        inter.append(i)

print(inter)
