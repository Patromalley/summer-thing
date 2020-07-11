import numpy as np
from matplotlib import pyplot
from scipy import optimize
import os
import pandas as pd
import io
from champion_dic import  Champion_values

print(Champion_values)

winrate = np.zeros([149, 149], dtype = int)



#12 is champ 19 is result, len(df.values[0])
#df = pd.read_csv('matchdata.csv',header=None, index_col=False)
#for i in  range(1,10):
   #print(i,df.values[i,12],df.values[i,19])
   #for j in  range(0,9):
