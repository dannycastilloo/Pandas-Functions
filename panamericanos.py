import pandas as pd

df = pd.read_csv('Panamericanos_Lima.csv')

# Obtener la sumatoria de los valores de una determinada columna y/o campo
def showTotal():
    result = df['Oro'].sum()
    return result

# Obtener el número de elementos
def showSize():
    rows, columns = df.shape
    result = rows * columns
    return result

# Obtener la media de los valores de una determinada columna y/o campo
def showMean():
    result = df['Oro'].mean()
    return result

# Obtener la media de los valores de una determinada columna y/o campo
def showRoundedMean():
    result = df['Oro'].mean().round(2)
    return result

# Obtener la mediana de los valores de una determinada columna y/o campo
def showMedian():
    result = df['Plata'].median()
    return result

# Obtener la moda de los valores de una determinada columna y/o campo
def showMode():
    result = df['Bronce'].mode()
    return result

# Obtener los percentiles (25,50,80,85) de los valores de una determinada columna y/o campo
def showPercentiles():
    result = df['Bronce'].quantile(0.85)
    return result

# Obtener la varianza de los valores de una determinada columna y/o campo
def showVariance():
    result = df['Oro'].var()
    return result

print(showVariance())