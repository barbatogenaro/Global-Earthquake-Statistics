import pandas as pd

terremoros = pd.read_csv("metodos\Global_Earthquake_Data.csv")

filas_columnas = terremoros.shape
print(filas_columnas)