##############
## IMPORTS  ##
##############

import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt
import subprocess

#############
## LECTURE ##
#############

# DESCOMPRESION DE ZIP
result = subprocess.run(["unzip", "/content/credit card fraud/archive.zip"], capture_output=False, text=False)

# Lectura PD
creditCard_df = pd.read_csv("/content/creditcard_2023.csv")

# Ojito
creditCard_df.head()

# Descripcion general del dataset
creditCard_df.describe()

# Verificamos nivel de desbalanceo de las clases
creditCard_df["Class"].value_counts()

# Identificamos valroes nulos
creditCard_df.isnull().sum()


# Identificacion rapida-visual de distribuciones
cols = creditCard_df.columns[1:-2]

# Cambio de nombre de df
credit_data = creditCard_df

# Calculo de matriz para los posteriores graficos
filas_para_multigraph = 9
columnas_para_multigraph = int(len(cols)/9)

# Generacion de malla para subplots
fig, axs = plt.subplots(nrows=filas_para_multigraph, ncols=columnas_para_multigraph, figsize=(15, 30))

# graficos
for ax,label in zip(axs.flat,cols):
    # Histogramas para tipos de clase en el mismo grafico
    ax.hist(credit_data[credit_data['Class']==0][label],bins = 100,color='blue',label='Legit' , alpha=0.7 , density=True)
    ax.hist(credit_data[credit_data['Class']==1][label],bins = 100,color='green',label='Fraudulent' , alpha=0.7 , density=True)
    ax.set_title(label,fontsize = 9)
    ax.legend()
  
plt.show()
