import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# Charger les données à partir d'un fichier CSV
sales_data = pd.read_csv("sales_data.csv")

# Afficher les informations générales sur les données
st.write("Informations générales sur les données :")
st.write(sales_data.shape)
st.write(sales_data.dtypes)
st.write(sales_data.describe())

# Créer une visualisation d'histogramme pour la distribution des quantités vendues
st.write("Distribution des quantités vendues :")
fig, ax = plt.subplots()
sns.histplot(sales_data["QUANTITY"], ax=ax)
st.pyplot(fig)

# Convertir la colonne de date en un type de données de date
sales_data["DATE"] = pd.to_datetime(sales_data["DATE"], format="%m/%d/%Y")

# Regrouper les données de ventes par date et calculer la somme de la quantité vendue pour chaque jour
daily_sales = sales_data.groupby("DATE").sum()["QUANTITY"]

# Créer un graphique de ligne de la quantité vendue en fonction de la date
fig, ax = plt.subplots()
ax.plot(daily_sales.index, daily_sales.values)
ax.set_xlabel("Date")
ax.set_ylabel("Quantité vendue")
ax.set_title("Évolution de la quantité vendue au fil du temps")
st.pyplot(fig)
# Regrouper les données de ventes par année et calculer la somme de la quantité vendue pour chaque année
yearly_sales = sales_data.groupby(sales_data["DATE"].dt.year)["QUANTITY"].sum()
# Créer un graphique à barres de la quantité de ventes par an
fig, ax = plt.subplots()
ax.bar(yearly_sales.index, yearly_sales.values)
ax.set_xlabel("Année")
ax.set_ylabel("Quantité vendue")
ax.set_title("Quantité de ventes par an")
st.pyplot(fig)
# Créer un graphique circulaire de la quantité de ventes par an
fig, ax = plt.subplots()
ax.pie(yearly_sales.values, labels=yearly_sales.index, autopct="%1.1f%%")
ax.set_title("Quantité de ventes par an")
st.pyplot(fig)
# Regrouper les données de ventes par mois et calculer la somme de la quantité vendue pour chaque mois
# Regrouper les données de ventes par mois et calculer la somme de la quantité vendue pour chaque mois
monthly_sales = sales_data.groupby(sales_data["DATE"].dt.strftime("%B %Y"))["QUANTITY"].sum()

# Créer un graphique à barres de la quantité de ventes par mois
fig, ax = plt.subplots()
ax.bar(monthly_sales.index, monthly_sales.values)
ax.set_xlabel("Mois")
ax.set_ylabel("Quantité vendue")
ax.set_title("Quantité de ventes par mois")
st.pyplot(fig)

# Regrouper les données de ventes par produit et calculer la somme de la quantité vendue pour chaque produit
product_sales = sales_data.groupby("PRODUCT ID")["QUANTITY"].sum()

# Définir la taille de la figure
fig = plt.figure(figsize=(10, 6))

# Créer un graphique à barres de la quantité de ventes par produit
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(product_sales.index, product_sales.values)
ax.set_xlabel("Produit")
ax.set_ylabel("Quantité vendue")
ax.set_title("Quantité de ventes par produit")
plt.xticks(rotation=90)

# Afficher le graphique à barres dans Streamlit
st.pyplot(fig)

# Regrouper les données de ventes par produit et par type de vente et calculer la somme de la quantité vendue pour chaque produit et chaque type de vente
sales_pivot = sales_data.pivot_table(index="PRODUCT ID", columns="SALE TYPE", values="QUANTITY", aggfunc="sum")

# Créer un graphique à barres empilé de la quantité de ventes par produit et par type de vente
fig, ax = plt.subplots()
sales_pivot.plot(kind="bar", stacked=True, ax=ax)
ax.set_xlabel("Produit")
ax.set_ylabel("Quantité vendue")
ax.set_title("Quantité de ventes par produit et par type de vente")
plt.xticks(rotation=90)

# Afficher le graphique à barres empilé dans Streamlit
st.pyplot(fig)



# Regrouper les données de ventes par type de vente et calculer la somme de la quantité vendue pour chaque type de vente
sale_type_sales = sales_data.groupby("SALE TYPE")["QUANTITY"].sum()

# Créer un graphique à barres de la quantité de ventes par type de vente
fig, ax = plt.subplots()
ax.bar(sale_type_sales.index, sale_type_sales.values)
ax.set_xlabel("Type de vente")
ax.set_ylabel("Quantité vendue")
ax.set_title("Quantité de ventes par type de vente")

# Afficher le graphique à barres dans Streamlit
st.pyplot(fig)

# Regrouper les données de ventes par mode de paiement et calculer la somme de la quantité vendue pour chaque mode de paiement
payment_mode_sales = sales_data.groupby("PAYMENT MODE")["QUANTITY"].sum()

# Créer un graphique à barres de la quantité de ventes par mode de paiement
fig, ax = plt.subplots()
ax.bar(payment_mode_sales.index, payment_mode_sales.values)
ax.set_xlabel("Mode de paiement")
ax.set_ylabel("Quantité vendue")
ax.set_title("Quantité de ventes par mode de paiement")

# Afficher le graphique à barres dans Streamlit
st.pyplot(fig)

# Regrouper les données de ventes par produit et par type de vente et calculer la somme de la quantité vendue pour chaque produit et chaque type de vente
sales_pivot = sales_data.pivot_table(index="PRODUCT ID", columns="SALE TYPE", values="QUANTITY", aggfunc="sum")

# Créer une carte thermique des quantités de ventes par produit et par type de vente
fig, ax = plt.subplots()
sns.heatmap(sales_pivot, annot=True, cmap="YlGnBu", fmt=".0f", ax=ax)
ax.set_xlabel("Type de vente")
ax.set_ylabel("Produit")
ax.set_title("Quantité de ventes par produit et par type de vente")

# Afficher la carte thermique dans Streamlit
st.pyplot(fig)
import streamlit as st
import pandas as pd
import plotly.express as px
data=sales_data

# Convertir la colonne date en format de date
data["DATE"] = pd.to_datetime(data["DATE"])
data=sales_data
# Ajouter des colonnes pour jour, mois et année
data["JOUR"] = data["DATE"].dt.day
data["MOIS"] = data["DATE"].dt.month
data["ANNEE"] = data["DATE"].dt.year

# Sidebar pour filtrer par produit ID, type de vente et mode de paiement
st.sidebar.title("Filtres")
product_id = st.sidebar.multiselect("Produit ID", sales_data["PRODUCT ID"].unique())
sale_type = st.sidebar.multiselect("Type de vente",sales_data["SALE TYPE"].unique())
payment_mode = st.sidebar.multiselect("Mode de paiement", sales_data["PAYMENT MODE"].unique())

# Filtrer les données
filtered_data = sales_data[(sales_data["PRODUCT ID"].isin(product_id)) & 
                     (sales_data["SALE TYPE"].isin(sale_type)) &
                     (sales_data["PAYMENT MODE"].isin(payment_mode))]

# Créer une visualisation de nuage de points pour la relation entre la quantité et le prix de vente
'''st.write("Relation entre la quantité et le prix de vente :")
fig, ax = plt.subplots()
sns.scatterplot(x="QUANTITY", y="PRICE", data=sales_data, ax=ax)
st.pyplot(fig)

st.write("Modèle de régression linéaire pour prédire les ventes futures :")
X = sales_data[["QUANTITY"]]
y = sales_data["SALES"]
model = LinearRegression()
model.fit(X, y)
quantity_input = st.number_input("Entrez la quantité vendue :", min_value=0, max_value=10000)
predicted_sales = model.predict([[quantity_input]])
st.write("Les ventes prévues pour la quantité vendue sont de :", predicted_sales)
st.write("Modèle de clustering pour identifier les meilleures ventes :")
X = sales_data[["QUANTITY", "PRICE"]]
model = KMeans(n_clusters=3)
model.fit(X)
sales_data["cluster"] = model.predict(X)
st.write(sales_data.groupby("cluster").mean())'''
