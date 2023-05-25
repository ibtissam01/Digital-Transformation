import streamlit as st
import pandas as pd
from fbprophet import Prophet

# Charger les données dans un DataFrame pandas
df = pd.read_csv('merged_data.csv')

# Convertir la colonne "DATE" au format "%Y-%m-%d"
df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')

# Créer un objet Prophet
m = Prophet()

# Ajouter une saisonnalité hebdomadaire
m.add_seasonality(name='weekly', period=7, fourier_order=3)

# Renommer les colonnes pour correspondre à la syntaxe de Prophet
df = df.rename(columns={'DATE': 'ds', 'revenue': 'y'})

# Entraîner le modèle
m.fit(df)

# Créer un DataFrame avec les dates futures
future = m.make_future_dataframe(periods=30)

# Faire des prévisions sur les dates futures
forecast = m.predict(future)

# Créer une application Streamlit
st.title('Prévisions de revenusavec Prophet')

# Afficher les prévisions
st.subheader('Prévisions')
st.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# Afficher les graphiques
st.subheader('Graphiques')
fig1 = m.plot(forecast)
st.pyplot(fig1)

fig2 = m.plot_components(forecast)
st.pyplot(fig2)
