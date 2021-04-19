import numpy as np
import pandas as pd
import random

def roll_dX(X):
 return random.choice(list(range(X)))+1

def roll_NdX(N,X):
 op=0
 for i in range(N):
  op+=roll_dX(X)
 return op

def exponential_dist(X):
 op=0
 while roll_dX(X)>1:
  op+=1
 return op
  

def gen_sharks():
 NShark=2+roll_dX(4)
 op=0
 for shark in range(NShark):
  op+=roll_dX(10)
 return op

def gen_demon_whale():
 return roll_NdX(17,12)

def gen_crabmonsters():
 return exponential_dist(80)

def gen_atlanteans():
 return 20 + roll_NdX(3,20)

def gen_alexandrians():
 return roll_dX(8)*roll_dX(8)*roll_dX(8) + roll_dX(20)

def gen_kraken():
 return roll_NdX(12,8)

def gen_brigands():
 return roll_NdX(4,8)

def gen_privateers():
 return roll_NdX(6,12)

def gen_nessie():
 return 40+roll_NdX(10,8)

def gen_harpy():
 return roll_dX(4)+roll_dX(8)+roll_dX(12)

def gen_water_elemental():
 return 73+roll_dX(12)


def approx_die_percentage(func, lim, N=10000):
 died=0
 for i in range(N):
  if func()>lim:
   died+=1
 return str((died/float(N))*100)+"%"

print("alexandrians: " + approx_die_percentage(gen_alexandrians, 100))
print("whales: " + approx_die_percentage(gen_demon_whale, 100))
print("crabs: " + approx_die_percentage(gen_crabmonsters, 100))
print("nessies: " + approx_die_percentage(gen_nessie, 100))

print("NICELY")
print("whales: " + approx_die_percentage(gen_demon_whale, 150))
print("crabs: " + approx_die_percentage(gen_crabmonsters, 200))
print("nessies: " + approx_die_percentage(gen_nessie, 110))

classificationLookup={
"alexandrians":"merpeople",
"atlanteans":"merpeople",
"brigands":"pirates",
"privateers":"pirates"}

def clookup(X):
 if X in classificationLookup:
  return classificationLookup[X]
 return X

funcLookup={
"sharks":gen_sharks,
"demon whale":gen_demon_whale,
"crabmonsters":gen_crabmonsters,
"atlanteans":gen_atlanteans,
"alexandrians":gen_alexandrians,
"kraken":gen_kraken,
"brigands":gen_brigands,
"privateers":gen_privateers,
"nessie":gen_nessie,
"harpy":gen_harpy,
"water elemental":gen_water_elemental}

dictForDf = {"month of departure":[], "direction":[], "encounter":[], "damage taken":[]}

peaceSelector = ["sharks"]*7+["demon whale"]*3+["crabmonsters"]*3+["atlanteans"]*3+["alexandrians"]*4+["kraken"]*4+["brigands"]*7+["privateers"]*2+["nessie"]*2+["harpy"]*3+["water elemental"]*4

print(len(peaceSelector))

strifeSelector = peaceSelector+["privateers"]*5

df=pd.DataFrame(dictForDf)

random.seed(0)

for year in [1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405]:
 print(year)
 for month in range(1, 12+1):
  nships=165+roll_NdX(3,10)
  for ship in range(nships):
   #First we find out what really happened . . .
   if (year,month)<(1401, 3):
    encounter = random.choice(strifeSelector)
   else:
    encounter = random.choice(peaceSelector)
   direction=random.choice(["northbound", "southbound"])
   dfunc = funcLookup[encounter]
   damage = dfunc()
   #and then . . .
   if damage>=100:
    newRow = {"month of departure":str(month)+"/"+str(year), "direction":direction, "encounter":"unknown", "damage taken":"100%+"}
   else:
    newRow = {"month of departure":str(month)+"/"+str(year), "direction":direction, "encounter":clookup(encounter), "damage taken":str(damage)+"%"}
   df=df.append(newRow, ignore_index=True)

print(df)
df.to_csv("dset.csv")


   
