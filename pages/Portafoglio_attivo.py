import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
import altair as alt
import matplotlib.pyplot as plt

st.markdown('<h1 style="color: #;">Portafoglio Long-term</h1>',
            unsafe_allow_html=True)




# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Liquidità', 'Mondiale', 'Dax', 'Oro'
sizes = [56.4, 15.7, 7.2, 20.9]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
col1, col2= st.columns(2)
col1.pyplot(fig1)
col2.metric("Rendimento Gennaio","1.95%" , "Totale " + "1.95%")



df = pd.DataFrame()
df["Strumenti"] = ["Liquidità","Vanguard FTSE All-World UCITS ETF - (USD) Accumulating ","Lyxor Dax","Wisdomtree Physical Gold"]
df["ISIN"] = ["--","IE00BK5BQT80","LU0252633754","JE00B1VS3770"]
df["Pesi"] = ["56.4%","15.7%","7.2%","20.9%"]

st.markdown('<h4 style="color: #;">Composizione Febbraio 2023</h4>',
            unsafe_allow_html=True)
st.dataframe(df)



