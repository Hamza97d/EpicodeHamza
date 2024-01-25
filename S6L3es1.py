import pandas as pd



""" Effettuiamo calcoliamo le informazioni statistiche base (numerosita, modie, mode, mediane, quartili, ecc) 
sulle colonne numeriche usando python """


wine= pd.read_csv("wine.csv", header= 0)

dt_wine= pd.DataFrame(wine)
#numeric_only= True

#numerosita wine
conteggio_righe= dt_wine.count()

#media wine
media_wine= dt_wine.mean(axis=0, numeric_only= True)

#moda wine
moda_wine= dt_wine.mode()


#mediane wine
mediana_wine= dt_wine.median(numeric_only=True)



#quartili wine
quartili_wine= dt_wine.quantile((0.25, 0.5, 0.7 ), numeric_only=True)


#MIN
minimo_wine= dt_wine.min()


#MAX
massimo_wine= dt_wine.max(numeric_only= True)
print(massimo_wine)







