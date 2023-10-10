import pandas as pd
import matplotlib.pyplot as plt

diz={"nomi":["paolo", "paolo", "andrea", "marta","agnese"], "genere":["maschio","maschio","maschio","femmina","femmina"],"professione":["attore","attore","cappellaio","professore","professore"], "eta":[30,35,20,50,60]}

dfPersone=pd.DataFrame.from_dict(diz)
print(dfPersone)
print("-"*50)

groupBy=dfPersone.groupby(by=["nomi"]).count()
print(groupBy)
print("-"*50)

print(groupBy.describe())
print("-"*50)

id = groupBy.idxmax()
print(id)
