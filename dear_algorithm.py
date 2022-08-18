#modules import
import pandas as pd
import numpy as np

#CHANGE FILE NAME HERE
filename = "database.xlsx"
#---------------------#

#importing data and conversion
df = pd.read_excel(filename,header= None)
df_head= df.iloc[-0, 1:]
df_material = df.iloc[1:, 1]
df_material= np.array(df_material)
df= np.array(df)

#initialisation
dfa = []
dfb = []
sumd = []
sumn = []

#user data extraction
print("Mark the properties that need to be weighed (1 for weightage and 0 for vice versa")
for i in range(2,len(df_head)+1):
    df_head[i] = input('1 or 0?\n') 


#weightage calculator   
for i in range(2,len(df_head)+1):
    if(int(df_head[i])==0):
        dfa.append(sum(1/df[1:,i]))
        dfb.append(1/(dfa[i-2]*df[1:,i]))
    else:
        dfa.append(sum(df[1:,i]))
        dfb.append(df[1:,i]/dfa[i-2])
dfb = np.transpose(dfb)
weighted = dfb*df[1:,2:]

#Ranking score
for j in range(0,len(df[1:,2])):
    r=0
    e=0
    for i in range(2,len(df_head)+1):
        if(int(df_head[i])==0):
            r = r + weighted[j,i-2]
        else:
            e = e + weighted[j,i-2]
    sumd.append(r)
    sumn.append(e)
sumd = np.array(sumd)
sumn = np.array(sumn)
mrpi = sumn/sumd

#ranking
mrpi_ = np.column_stack ((df_material,mrpi))
mrpisorted = mrpi_[mrpi_[:,1].argsort()[::-1]]

#output file
df_out = pd.DataFrame(mrpisorted)
df_out.to_csv("Ranked.csv" ,index = False)





 
