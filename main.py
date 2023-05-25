import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

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


# Convertir la colonne de dates en nombres réels
data['DATE'] = pd.to_datetime(data['DATE'])
data['DATE'] = data['DATE'].apply(lambda x: x.to_julian_date())


# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(data['DATE'], data['revenue'], test_size=0.2, random_state=0)

# Créer le modèle de régression linéaire
regressor = LinearRegression()

# Entraîner le modèle
X_train = X_train.values.reshape(-1, 1)
y_train = y_train.values.reshape(-1, 1)
regressor.fit(X_train, y_train)

# Prédire les ventes pour l'ensemble de test
X_test = X_test.values.reshape(--1, 1)
y_pred = regressor.predict(X_test)

# Évaluer les performances du modèle
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Afficher les performances du modèle
st.write('Performance du modèle')
st.write('MSE :', mse)
st.write('R2 score :', r2)

# Visualiser les résultats
st.subheader('Visualiser les résultats')
plt.figure(figsize=(10,6))
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.xlabel('Date (jour julien)')
plt.ylabel('Revenu')
plt.title('Régression linéaire pour prédire les ventes en fonction de la date')
st.pyplot()

