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
