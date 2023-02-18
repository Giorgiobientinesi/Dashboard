import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
import altair as alt
import matplotlib.pyplot as plt
import bs4
from bs4 import BeautifulSoup
import requests
st.set_option('deprecation.showPyplotGlobalUse', False)


commodities = {"Platino":["800-1500","1200-2000","900-1100","40","4%","PL=F",1100,900,1200],
               "Oro":["700-1200","1200-1600","1100-1300","55","5%","GC=F",1200,1000,1200],
                "Argento":["13-20","15-25","14-17","0.6","5%","SI=F",17,14,15],
               "Cacao":["2000-3000","2500-4000","1900-2600","125","5%","CC=F",2600,1900,2500],
               "Cotone":["60-120","70-150","70-80","3.5","4%","CT=F",80,70,70],
               "Alluminio":["1500-2500","2000-3500","1600-2000","70","4%","ALI=F",2000,1600,2000],
               "Zucchero":["10-20","15-25","10-15","0.7","6%","SB=F",15,10,15],
               "Caffè":["100-200","150-300","90-140","4.5","4%","KC=F",140,90,150],
               "Nickel":["7000-12000","9000-15000","10-15","da vedere","da vedere","NICK.L",15,10,9000],
               "Piombo":["1000-2000","1500-2500","13-16","da vedere","da vedere","LEAD.MI",16,13,1500],
               "Zinco":["500-2500","1500-3000","4-6","da vedere","da vedere","ZINC.MI",6,4,1500],
               "Rame":["5000-8000","7000-12000","18-25","da vedere","da vedere","COPA.MI",25,18,7000],
               "Petrolio":["30-80","50-100","CL=F",50],
               "Gas Naturale":["2-5","3-7","NG=F",3]}
#prezzo,prezzo all in, scala buona, vendita, profitto, ticker, massimo scala, minimo scala, minimo all in

nomi = ["Nickel", "Lead", "Zinc", "Copper"]
prezzi = []

for el in nomi:
    url = "https://www.lme.com/Metals/Non-ferrous/LME-{}#Trading+day+summary".format(el)
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    price = soup.find("span", {"class": "hero-metal-data__number"})
    price = price.text.split()[0]
    prezzi.append(price)



with st.sidebar:
    add_radio = st.selectbox(
        "Commodities",
        ("Platino","Oro","Argento","Cacao","Cotone","Alluminio","Zucchero","Caffè","Nickel","Piombo","Zinco","Rame","Petrolio","Gas Naturale")
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

    if strumento not in ["Petrolio","Gas Naturale","Nickel","Piombo","Zinco","Rame"]:
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
        if data["Close"][-1] > commodities[strumento][8]:
            col4.metric("Prezzo attuale", str(data["Close"][-1])[:6], str((commodities[strumento][8]-data["Close"][-1])/data["Close"][-1]*100)[:5]+ "%, rispetto All in")
        else:
            col4.metric("Prezzo attuale", str(data["Close"][-1])[:6],"In linea")

        plt.plot(data["Close"], label='Prezzi',color="black")
        plt.axhline(commodities[strumento][6], color='red', linestyle='--', label='Massimo valore scala')
        plt.axhline(commodities[strumento][7], color='green', linestyle='--', label='Minimo valore scala')


        plt.legend()

        st.pyplot()

    elif strumento in ["Petrolio","Gas Naturale"]:
        st.markdown('<h1 style="color: #;">Scheda tecnica {}</h1>'.format(strumento),
                    unsafe_allow_html=True)
        st.write(" ")



        PLT = yf.Ticker(commodities[strumento][2])

        current_dateTime = datetime.now()

        data = pd.DataFrame(PLT.history(start="2008-01-01", end=current_dateTime))


        col1, col2, col3,col4 = st.columns(4)

        st.write(" ")
        col1.metric("Costo di Produzione", commodities[strumento][0], "all in " + commodities[strumento][1])
        if data["Close"][-1] > commodities[strumento][3]:
            col3.metric("Prezzo attuale", str(data["Close"][-1])[:6], str((commodities[strumento][3]-data["Close"][-1])/data["Close"][-1]*100)[:5]+ "%, rispetto All in")
        else:
            col3.metric("Prezzo attuale", str(data["Close"][-1])[:6],"In linea")

        plt.plot(data["Close"], label='Prezzi',color="black")
        plt.axhline(commodities[strumento][3], color='red', linestyle='--', label='Minimo all-in')

        plt.legend()

        st.pyplot()
    elif strumento in ["Nickel","Piombo","Zinco","Rame"]:


        prezzi_dict = {"Nickel": prezzi[0], "Piombo": prezzi[1], "Zinco": prezzi[2],"Rame":prezzi[3]}


        st.markdown('<h1 style="color: #;">Scheda tecnica {} , prezzi ETC</h1>'.format(strumento),
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


        if float(prezzi_dict[strumento]) > commodities[strumento][8]:
            col4.metric("Prezzo attuale", str(float(prezzi_dict[strumento]))[:7], str((commodities[strumento][8]-float(prezzi_dict[strumento]))/float(prezzi_dict[strumento])*100)[:5]+ "%, rispetto All in")
        else:
            col4.metric("Prezzo attuale", str(prezzi_dict[strumento])[:6],"In linea")

        plt.plot(data["Close"], label='Prezzi',color="black")
        plt.axhline(commodities[strumento][6], color='red', linestyle='--', label='Massimo valore scala')
        plt.axhline(commodities[strumento][7], color='green', linestyle='--', label='Minimo valore scala')


        plt.legend()

        st.pyplot()

        col1.write("Prezzo attuale: " +str(data["Close"][-1])[:4])









if add_radio != "Nessuna":
    scheda_tecnica(add_radio)
else:
    st.write(" ")









monitoraggio = {"Platino":["PL=F",1200],
               "Oro":["GC=F",1200],
                "Argento":["SI=F",15],
               "Cacao":["CC=F",2500],
               "Cotone":["CT=F",70],
               "Alluminio":["ALI=F",2000],
               "Zucchero":["SB=F",15],
               "Caffè":["KC=F",150],
               "Nickel":["NICK.L",9000],
               "Piombo":["LEAD.MI",1500],
               "Zinco":["ZINC.MI",1500],
               "Rame":["COPA.MI",7000],
               "Petrolio":["CL=F",50],
               "Gas Naturale":["NG=F",3]}


st.sidebar.write(" ")


df = pd.DataFrame()

strumento = []
prezzi_attuali = []
differenze = []

for j in monitoraggio.keys():
    if j not in ["Nickel","Piombo","Zinco","Rame"]:
        strumento.append(j)
        PLT = yf.Ticker(monitoraggio[j][0])
        current_dateTime = datetime.now()
        dati = pd.DataFrame(PLT.history(start="2023-01-01", end=current_dateTime))

        prezzi_attuali.append(str(float(dati["Close"][-1]))[:6])

        diff = (monitoraggio[j][1] - float(str(dati["Close"][-1])[:6]))/float(str(dati["Close"][-1])[:6])
        differenze.append(diff)

    else:
        strumento.append(j)

        prezzi_dict = {"Nickel": prezzi[0], "Piombo": prezzi[1], "Zinco": prezzi[2],"Rame":prezzi[3]}


        prezzi_attuali.append(prezzi_dict[j])

        diff = (monitoraggio[j][1] - float(str(prezzi_dict[j])[:6])) / float(str(prezzi_dict[j])[:6])
        differenze.append(diff)



differenze_perc = []
for element in differenze:
    differenze_perc.append(str(element*100)[:5] + "%")


df["strumento"] = strumento
df["prezzo"] = prezzi_attuali
df["differenze_perc"] = differenze_perc
df["differenze"] = differenze

df = df.sort_values(by='differenze', ascending=False)

df = df.drop('differenze', axis=1)

st.sidebar.dataframe(df)
