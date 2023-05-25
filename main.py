import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)
# Charger les données
data = pd.read_csv("merged_data.csv")

# Afficher les données brutes
st.header("Données brutes")
st.write(data.head())


# Afficher des informations sur les données
st.write('Informations sur les données')
st.write(data.info())

# Identifier les valeurs aberrantes
st.subheader('Identifier les valeurs aberrantes')
plt.figure(figsize=(10,6))
sns.boxplot(x='QUANTITY', data=data)
st.pyplot()

# Traiter les valeurs manquantes
st.subheader('Traiter les valeurs manquantes')
st.write(data.isnull().sum())

# Résumé statistique des données
st.header("Résumé statistique")
st.write(data.describe())



# Identifier les relations entre les variables
st.subheader('Identifier les relations entre les variables')
sns.pairplot(data[['QUANTITY','SELLING PRICE','revenue']])
st.pyplot()

st.write('Corrélation entre les variables')
st.write(data[['QUANTITY','SELLING PRICE','revenue']].corr())

# Visualiser les distributions devariables
st.subheader('Visualiser les distributions de variables')
plt.figure(figsize=(10,6))
sns.histplot(data['SELLING PRICE'], bins=20)
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


