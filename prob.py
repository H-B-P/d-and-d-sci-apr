
import math

#shamelessly ripped off from https://math.stackexchange.com/questions/933871/probability-of-each-outcome-from-dice-notation, I won't pretend to understand or care about the proof.

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

def get_prob_4d6_gives_X(X):
 num=0
 denom=0
 for a in [1,2,3,4,5,6]:
  for b in [1,2,3,4,5,6]:
   for c in [1,2,3,4,5,6]:
    for d in [1,2,3,4,5,6]:
     denom+=1
     if (a+b+c+d)==X:
      num+=1
 return float(num)/float(denom)

print(get_prob_4d6_gives_X(12))
print(get_prob_ndm_gives_X(4,6,12))



print(get_prob_4d6_gives_X(17))
print(get_prob_ndm_gives_X(4,6,17))

#OK GREAT IT WORKS

#Nessie can kill

print("NESSIE")

def get_nessie_given_guns(guns):
 limit = 100/(1-0.1*guns)
 print(limit)
 die=0
 live=0
 for X in range(200):
  p = get_prob_ndm_gives_X(10,8, X)
  if (X+40)>=limit:
   die+=p
  else:
   live+=p
 return live, die

print(get_nessie_given_guns(0))
print(get_nessie_given_guns(1))
print(get_nessie_given_guns(2))
print(get_nessie_given_guns(3))

#whales can kill

print("WHALES")

wha=[]

def get_whale_given_oars(oars):
 limit = 100/(1-0.02*oars)
 print(limit)
 die=0
 live=0
 for X in range(200):
  p = get_prob_ndm_gives_X(17,12, X)
  if X>=limit:
   die+=p
  else:
   live+=p
 return live, die


for i in range(21):
 wha.append(get_whale_given_oars(i)[1])

print(wha)


#crabs can kill

print("CRABS")

def get_crabs_given_carp(carp):
 limit=100*(1+carp)
 die = math.pow(79.0/80.0, limit)
 live = 1-die
 return live, die

print(get_crabs_given_carp(0))
print(get_crabs_given_carp(1))

#alexandrians can kill

print("ALEXANDRIANS")

def get_alexandrians():
 limit=100
 bit=1.0/(8*8*8*20)
 die=0
 live=0
 for i in [1,2,3,4,5,6,7,8]:
  for j in [1,2,3,4,5,6,7,8]:
   for k in [1,2,3,4,5,6,7,8]:
    for q in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
     if (i*j*k+q)>=limit:
      die+=bit
     else:
      live+=bit
 return live, die

print(get_alexandrians())
