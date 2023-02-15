import streamlit as st
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

"Vamos a mostrar un ejemplo de como funciona un modelo de prediccion."
"Para eso vamos a usar un dataset con datos del Titanic y su hundimiento"
"Existen registros de datos de los pasajes del Titanic y sus caracteristicas"
"Tomando como referencia estas caracteristicas queremos calcular que le hubiese"
"pasado a un hipotetico pasajero inventado."
titanic = sns.load_dataset('titanic')

"Aqui tenemos un ejemplo de la informacion cruda disponible."

titanic

"Como vemos hay varias columnas, algunas con datos numericos, otros categoricos y algunos redundantes."
"Lo primero que vamos a hacer es seleccionar las columnas que nos parecen relevantes, por ejemplo 'embarked'"
" y 'embarked_town' son lo mismo."

selected_columns = ['survived','pclass','sex','age','sibsp','parch','fare','embarked']

"Las columnas que elegimos conservar son:"

st.write(selected_columns)

class Columns_selector(BaseEstimator, TransformerMixin):
    
    def __init__(self,columns):
        self.columns = columns
    
    def fit(self,X,y=None):
        pass
        return self
    
    def transform(self, X, y=None):
        return X[self.columns]        

"Una vez que filtramos los datos seleccionando solo las columnas que deseamos nos queda asi:"

columns_selector = Columns_selector(selected_columns)
titanic_filtrado = columns_selector.fit_transform(titanic)
titanic_filtrado

"Un problema que va a surgir al procesar los datos es que hacer con los datos faltantes"
"por ejemplo en el registro 5 la persona no tiene dato de edad"
"visualicemos con un mapa de calor cuantos datos faltan en cada columna"


fig = plt.figure(figsize=(10, 4))
sns.heatmap(titanic_filtrado.isna(), cbar=False)
st.pyplot(fig)

"Vemos que el problema esta solamente en la columna age. En este caso tenemos tres opciones tipicas."
"Podemos descartar los registros sin datos (perderiamos parte relevante de la informacion), podriamos"
"imputar todos los registros sin datos por un valor medio, o podriamos imputarlos por valores al azar"
"tomados del propio dataset. Mas adelante vamos a probar que sucede en cada uno de los casos. Pero antes"
"veamos que rangos y valores tiene cada columna numerica."

st.write(titanic_filtrado.describe(include = np.number))

"Para las demas columnas podemos ver que valores aparecen mas"
for column in [column for column in titanic_filtrado.columns if titanic_filtrado[column].dtype == 'object']:
    st.write(titanic_filtrado[column].value_counts())

"Vemos que son todos numeros razonables."

st.image("https://444prophecynews.com/wp-content/uploads/2020/12/textgram_1608075611.png")


"Vamos a saltar a lo que ya tenemos entrenado"

with open('dummies_order.pkl', 'rb') as f_dummy:
    dummies_encoder = pickle.load(f_dummy)

st.write(dummies_encoder)

# Cargamos el modelos desde nuestra carpeta local en el servidor usando Pickle
with open('./math_model.pkl', 'rb') as f_math:
    modelo_matematicas = pickle.load(f_math)

st.write(modelo_matematicas.coef_)

st.write(modelo_matematicas.predict([[0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,1,1]]))

values = []
for name in dummies_encoder:
    values.append(st.checkbox(name))

st.write(values)

"El valor del modelo para el caso seleccionado es: "
st.write(modelo_matematicas.predict([values]))