import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
data = pd.read_csv("merged_data.csv")

# Afficher les données brutes
st.header("Données brutes")
st.write(data)

# Résumé statistique des données
st.header("Résumé statistique")
st.write(data.describe())
# Importer les bibliothèques nécessaires
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
@st.cache
def load_data():
    data = pd.read_csv('ventes.csv')
    return data

data = load_data()

# Afficher les premières lignes des données
st.subheader('Examiner les données')
st.write(data.head())

# Afficher des informations sur les données
st.write('Informations sur les données')
st.write(data.info())

# Identifier les valeurs aberrantes
st.subheader('Identifier les valeurs aberrantes')
plt.figure(figsize=(10,6))
sns.boxplot(x='Quantité', data=data)
st.pyplot()

# Traiter les valeurs manquantes
st.subheader('Traiter les valeurs manquantes')
st.write(data.isnull().sum())

# Identifier les relations entre les variables
st.subheader('Identifier les relations entre les variables')
sns.pairplot(data[['Quantité', 'Buying Price', 'Selling Price', 'revenue']])
st.pyplot()

st.write('Corrélation entre les variables')
st.write(data[['Quantité', 'Buying Price', 'Selling Price', 'revenue']].corr())

# Visualiser les distributions devariables
st.subheader('Visualiser les distributions de variables')
plt.figure(figsize=(10,6))
sns.histplot(data['Selling Price'], bins=20)
st.pyplot()

# Identifier les tendances temporelles
st.subheader('Identifier les tendances temporelles')
data['DATE'] = pd.to_datetime(data['DATE'])
data.set_index('DATE', inplace=True)

plt.figure(figsize=(15,5))
sns.lineplot(x=data.index, y='revenue', data=data)
st.pyplot()

# Identifier les catégories de produits les plus vendues
st.subheader('Identifier les catégories de produits les plus vendues')
plt.figure(figsize=(10,6))
sns.countplot(x='CATEGORY', data=data)
st.pyplot()

# Identifier les modes de paiement les plus populaires
st.subheader('Identifier les modes de paiement les plus populaires')
plt.figure(figsize=(10,6))
sns.countplot(x='PAYMENT MODE', data=data)
st.pyplot()
# Histogramme des ventes
st.header("Histogramme des ventes")
plt.hist(data["revenue"])
st.pyplot()

# Diagramme circulaire des catégories de produits
st.header("Diagramme circulaire des catégories de produits")
categories = data.groupby("CATEGORY")["revenue"].sum()
plt.pie(categories, labels=categories.index)
st.pyplot()

# Matrice de corrélation
st.header("Matrice de corrélation")
corr = data.corr()
sns.heatmap(corr, annot=True)
st.pyplot()

