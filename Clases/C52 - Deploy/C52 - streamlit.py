import streamlit as st
from sklearn.base import BaseEstimator, TransformerMixin
import seaborn as sns
import matplotlib.pyplot as plt
import pickle


titanic = sns.load_dataset('titanic')

st.write(titanic)


selected_columns = ['survived','pclass','sex','age','sibsp','parch','fare','embarked']


st.write(selected_columns)

class Columns_selector(BaseEstimator, TransformerMixin):
    
    def __init__(self,columns):
        self.columns = columns
    
    def fit(self,X,y=None):
        pass
        return self
    
    def transform(self, X, y=None):
        return X[self.columns]      

columns_selector = Columns_selector(selected_columns)
titanic_filtrado = columns_selector.fit_transform(titanic)
st.write(titanic_filtrado)


fig = plt.figure(figsize=(10, 4))
sns.heatmap(titanic_filtrado.isna(), cbar=False)
st.pyplot(fig)

with open('dummies_order.pkl', 'rb') as f_dummy:
    dummies_encoder = pickle.load(f_dummy)

st.write(dummies_encoder)

# Cargamos el modelos desde nuestra carpeta local en el servidor usando Pickle
with open('./math_model.pkl', 'rb') as f_math:
    modelo_matematicas = pickle.load(f_math)

st.write(modelo_matematicas.coef_)

st.write(f'El modelo predice un valor de {modelo_matematicas.predict([[0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,1,1]])[0]}')


values = []
for name in dummies_encoder:
    values.append(st.checkbox(name))

#st.write(values)

"El valor del modelo para el caso seleccionado es: "
st.write(modelo_matematicas.predict([values])[0])