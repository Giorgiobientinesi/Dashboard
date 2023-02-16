import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
import altair as alt
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


commodities = {"Platino":["800-1500","1200-2000","900-1100","40","4%","PL=F",1100,900,1200],
               "Oro":["700-1200","1200-1600","1100-1300","55","5%","GC=F",1200,1000,1200],
                "Argento":["13-20","15-25","14-17","0.6","5%","SI=F",17,14,15],
               "Cacao":["2000-3000","2500-4000","1900-2800","125","5%","CC=F",2800,1900,2500],
               "Cotone":["60-120","70-150","60-90","3.5","4%","CT=F",90,60,70],
               "Alluminio":["1500-2500","2000-3500","1600-2000","70","4%","ALI=F",2000,1600,2000],
               "Zucchero":["10-20","15-25","10-15","0.7","6%","SB=F",15,10,15],
               "Caffè":["50-80","70-120","90-140","4.5","4%","KC=F",140,90,70],
               "Petrolio":["30-80","50-100","CL=F",50],
               "Gas Naturale":["2-5","3-7","NG=F",3]}
#prezzo,prezzo all in, scala buona, vendita, profitto, ticker, massimo scala, minimo scala, minimo all in





with st.sidebar:
    add_radio = st.selectbox(
        "Commodities",
        ("Platino","Oro","Argento","Cacao","Cotone","Alluminio","Zucchero","Caffè","Petrolio","Gas Naturale")
    )

st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-image: linear-gradient(to right, #5b61f9 , #5b61f9);
        }
    </style>""",
    unsafe_allow_html=True,
)

def scheda_tecnica(strumento):

    if strumento != "Petrolio" and strumento != "Gas Naturale":
        st.markdown('<h1 style="color: #;">Scheda tecnica {}</h1>'.format(strumento),
                    unsafe_allow_html=True)
        st.write(" ")



        PLT = yf.Ticker(commodities[strumento][5])

        current_dateTime = datetime.now()

        data = pd.DataFrame(PLT.history(start="2008-01-01", end=current_dateTime))


        col1, col2, col3,col4 = st.columns(4)

        st.write(" ")

        col1.metric("Costo di Produzione", commodities[strumento][0],"all in " +commodities[strumento][1])
        col2.metric("Scala attiva", commodities[strumento][2])
        col3.metric("Ottimo di vendita", commodities[strumento][3], commodities[strumento][4])
        if data["Close"][-1] >commodities[strumento][6] or data["Close"][-1] < commodities[strumento][7]:
            col4.metric("Prezzo attuale", str(data["Close"][-1])[:6],str((data["Close"][-1]-commodities[strumento][6])/commodities[strumento][6]*100)[:4]+ "%")
        else:
            col4.metric("Prezzo attuale", str(data["Close"][-1])[:6],"In linea")

        plt.plot(data["Close"], label='Prezzi',color="black")
        plt.axhline(commodities[strumento][6], color='red', linestyle='--', label='Massimo valore scala')
        plt.axhline(commodities[strumento][7], color='green', linestyle='--', label='Minimo valore scala')


        plt.legend()

        st.pyplot()

    else:
        st.markdown('<h1 style="color: #;">Scheda tecnica {}</h1>'.format(strumento),
                    unsafe_allow_html=True)
        st.write(" ")



        PLT = yf.Ticker(commodities[strumento][2])

        current_dateTime = datetime.now()

        data = pd.DataFrame(PLT.history(start="2008-01-01", end=current_dateTime))


        col1, col2, col3,col4 = st.columns(4)

        st.write(" ")
        col1.metric("Costo di Produzione", commodities[strumento][0], "all in " + commodities[strumento][1])
        col2.metric("Prezzo attuale",str(data["Close"][-1])[:5])
        plt.plot(data["Close"], label='Prezzi',color="black")
        plt.axhline(commodities[strumento][3], color='red', linestyle='--', label='Minimo all-in')

        plt.legend()

        st.pyplot()






if add_radio != "Nessuna":
    scheda_tecnica(add_radio)
else:
    st.write(" ")
