# -*- coding: utf-8 -*-
"""
Created on Wed May 26 18:01:38 2021

@author: PRANAV
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)

df1 = pd.read_excel(r"C:\Users\PRANAV\Desktop\Project\no of customer per month.xlsx")
salepermonth = pd.read_csv(r"C:\Users\PRANAV\Desktop\Project\salepermonth.csv")
df = pd.read_csv(r"C:\Users\PRANAV\Desktop\Project\df_rfm.csv")
retail = pd.read_excel(r"C:\Users\PRANAV\Desktop\Project\sample_data.xlsx")

st.title('Customer Likelihood Prediction Analysis')
nav = st.sidebar.radio('Pages',['Home','Prediction'])
if nav == 'Home':
    st.header("Data Set Details:")
    st.markdown(''' ##### sample dataset''')
    st.dataframe(retail)
    st.markdown(''' ### Number of customer per month ''')
    st.bar_chart(df1)
    

if nav == 'Prediction':
    st.header('Prediction')
    
    x = st.number_input("CustomerID: ",min_value=salepermonth['CustomerID'].min(),max_value=salepermonth['CustomerID'].max())
    z = pd.DataFrame(df.loc[df['CustomerID'] == x])
    
    if st.button("Predict"):
        if z.iloc[0,11] == 2:
            st.success('yes')
        else:
            st.info('NO')
    st.subheader("RFM Score")
    y = salepermonth.loc[salepermonth['CustomerID'] == x]
    y = y.drop(y.iloc[:,0:1],axis = 1)
   
    st.dataframe(z)
    
    # Plotting Graph
    st.markdown("Number of month per customer")
    fig = plt.figure(figsize = (20, 12))
    month = ['Dec-2010', 'Jan-2011', 'Feb-2011', 'Mar-2011', 'Apr-2011', 'May-2011', 'Jun-2011', 'Jul-2011',
         'Aug-2011', 'Sep-2011', 'Oct-2011', 'Nov-2011', 'Dec-2011']
    # creating the bar plot
    plt.plot(month,y.iloc[0] ,color ='orange',width = 0.5)
    plt.xlabel("CustomerID: {}".format(x))
    plt.ylabel("Money Spent")
    st.pyplot()
    st.write("Thank You")