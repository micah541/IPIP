import pandas as pd 
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib.pyplot as plt
import time


df = pd.read_table("IPIP120.dat")  #did not work for me 

#I had trouble reading this, so instead 
f = open("IPIP120.dat", "r")
p = f.read()
p = p.split('\r\n')
sex = [i[5] for i in p[:-1]]
datastrings = [i[-120:] for i in p[:-1]]
datastringsplit = [list(d) for d in datastrings]
df = pd.DataFrame(datastringsplit, columns = ['I'+str(n+1) for n in range(120)])
df['sex'] = sex

## to get into pandas format
import pyreadstat

df, meta = pyreadstat.read_por("IPIP300.por")


df.to_csv("300.csv")




df = pd.read_csv("300.csv")
#men = df[df['sex']==1]
#sample_men = men.sample(n=50000)

for i in range(11):
    df.drop(df.columns[0], axis = 1, inplace=True)

X = df.as_matrix()

batch = 619


def getmu(v):
    VV = sorted(v)
    return(VV[2]/VV[1])

mus=[]
for i in range(len(X)/batch):
    tt = time.time()
    Y = X[batch*i:batch*(i+1)]
    dists = euclidean_distances(Y,X)
    mus += [getmu(vec) for vec in dists]
    print i
    print time.time()-tt

##  implement the algorith following equation (7) at https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5610237/

N = len(mus)
mui = [np.log(mm) for mm in mus]
mux = [-np.log(1-float(i)/N) for i in range(N)]
mui = sorted(mui)

## fit with 85%
np.polyfit(mui[0:85*N/100],mux[0:85*N/100],1)
## fit with 90%

np.polyfit(mui[0:90*N/100],mux[0:90*N/100],1)
#save for later 
np.savetxt("all_mus", mus)

#look at pictures


plt.scatter(mui,mux)
plt.show()


