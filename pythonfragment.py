import pandas as pd 
import numpy as np
import time
from sklearn.metrics.pairwise import euclidean_distances 


#reading the 120 set

f = open("IPIP120.dat", "r")
p = f.read()
p = p.split('\r\n')
sex = [i[6] for i in p[:-1]]
datastrings = [i[-120:] for i in p[:-1]]
datastringsplit = [list(d) for d in datastrings]
datastringsplit = [[int(a) for a in b] for b in datastringsplit]
df = pd.DataFrame(datastringsplit, columns = ['I'+str(n+1) for n in range(120)])
df['sex'] = sex

#men = df[df['sex']=='1']


#reading the 300 set
df, meta = pyreadstat.read_por("IPIP300.por")

for i in range(11):
    df.drop(df.columns[0], axis = 1, inplace=True)


df = df.sample(n=60000)  #taking a sample


X = df.as_matrix() 
#experimenting with noise
#noise = np.random.randn(X.shape[0], X.shape[1])/100
#X = X+noise

batch = 60


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


np.savetxt("sample_mus", mus)  


##  implement the algorithm of Elena Facco, Maria d’Errico, Alex Rodriguez, and Alessandro Laio, following equation (7) at https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5610237/

N = len(mus)
mui = [np.log(mm) for mm in mus]
mux = [-np.log(1-float(i)/N) for i in range(N)]
mui = sorted(mui)

#linear regression

np.polyfit(mui[0:85*N/100],mux[0:85*N/100],1)
np.polyfit(mui[0:90*N/100],mux[0:90*N/100],1)
np.polyfit(mui[0:95*N/100],mux[0:95*N/100],1)
np.polyfit(mui[0:80*N/100],mux[0:80*N/100],1)

#looking at the picture of graph

#plt.scatter(mui[0:90*N/100],mux[0:90*N/100])
plt.scatter(mui,mux)
plt.show()

