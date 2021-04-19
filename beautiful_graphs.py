import numpy as np
import pandas as pd
import math

import plotly.express as px
import plotly.graph_objects as go

def comb(a,b):
 if a<0 or b<0:
  return 0
 return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))

def get_prob_ndm_gives_X(n,m,X):
 mult=1.0/math.pow(m,n)
 amt=0
 for k in range(n+1):
  addon= comb(X-1-k*m, X-n-k*m)*comb(n,k)*math.pow(-1,k)
  amt+=addon
 return amt*mult

def gimme_sharks():
 op = [0]*201
 for i in [3,4,5,6]:
  for x in range(101):
   op[x]+=0.25*get_prob_ndm_gives_X(i,10,x)
 return op

def gimme_whales():
 op = [0]*201
 for x in range(201):
  op[x]=get_prob_ndm_gives_X(17,12,x)
 return op

def gimme_crabs():
 op=[0]*201
 for x in range(201):
  op[x]=math.pow(79.0/80.0,x)*1.0/80.0
 return op

def gimme_atlanteans():
 op=[0]*201
 for x in range(201):
  op[x]=get_prob_ndm_gives_X(3,20,x-20)
 return op

def gimme_alexandrians():
 op=[0]*201
 iota=1.0/float(8*8*8*20)
 for i in [1,2,3,4,5,6,7,8]:
  for j in [1,2,3,4,5,6,7,8]:
   for k in [1,2,3,4,5,6,7,8]:
    for q in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
     tot=i*j*k+q
     if tot<200:
      op[tot]+=iota
 return op

def gimme_kraken():
 op=[0]*201
 for x in range(101):
  op[x]=get_prob_ndm_gives_X(12,8,x)
 return op

def gimme_brigands():
 op=[0]*201
 for x in range(101):
  op[x]=get_prob_ndm_gives_X(4,8,x)
 return op
 
def gimme_privateers():
 op=[0]*201
 for x in range(101):
  op[x]=get_prob_ndm_gives_X(6,12,x)
 return op

def gimme_nessie():
 op=[0]*201
 for x in range(201):
  op[x]=get_prob_ndm_gives_X(10,8,x-40)
 return op

def gimme_harpy():
 op=[0]*201
 iota=1.0/float(4*8*12)
 for i in [1,2,3,4]:
  for j in [1,2,3,4,5,6,7,8]:
   for k in [1,2,3,4,5,6,7,8,9,10,11,12]:
    op[i+j+k]+=iota
 return op

def gimme_elementals():
 op=[0]*201
 for x in [74,75,76,77,78,79,80,81,82,83,84,85]:
  op[x]=1.0/12.0
 return op

def remains(op):
 return 1-sum(op)

def kills(op):
 return sum(op[100:])+remains(op)

def graph(op, name):
 fig = px.bar(x=list(range(201)), y=op, labels={'x':'damage (%)', 'y':'frequency'}, title="True distribution for "+name)
 fig.add_shape(
        type='line',
        x0=100,
        y0=0,
        x1=100,
        y1=max(op),
        line=dict(
            color='Red',
        )
 )
 fig.show()

print("sharks")
op=gimme_sharks()
graph(op, "sharks")
print(remains(op), kills(op))

print("whales")
op=gimme_whales()
graph(op, "whales")
print(remains(op), kills(op))
WHALE_KILLS=3*kills(op)


print("crabs")
op=gimme_crabs()
graph(op, "crabs")
print(remains(op), kills(op))
CRAB_KILLS=3*kills(op)

print("atlanteans")
op=gimme_atlanteans()
graph(op, "atlanteans")
print(remains(op), kills(op))

print("alexandrians")
op=gimme_alexandrians()
graph(op, "alexandrians")
print(remains(op), kills(op))
MER_KILLS=4*kills(op)

print("kraken")
op=gimme_kraken()
graph(op, "kraken")
print(remains(op), kills(op))

print("brigands")
op=gimme_brigands()
graph(op, "brigands")
print(remains(op), kills(op))

print("privateers")
op=gimme_privateers()
graph(op, "privateers")
print(remains(op), kills(op))

print("nessie")
op=gimme_nessie()
graph(op, "nessie")
print(remains(op), kills(op))
NESS_KILLS=2*kills(op)

print("harpy")
op=gimme_harpy()
graph(op, "harpy")
print(remains(op), kills(op))

print("elementals")
op=gimme_elementals()
graph(op, "elementals")
print(remains(op), kills(op))




denom = WHALE_KILLS+CRAB_KILLS+MER_KILLS+NESS_KILLS

print("WHALE, CRAB, MER, NESS")
print(WHALE_KILLS/denom, CRAB_KILLS/denom, MER_KILLS/denom, NESS_KILLS/denom)



