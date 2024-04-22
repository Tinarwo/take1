import streamlit as st
import pandas as pd
import pickle
import numpy
import time

def main():
    html_temp=""" 
   <div style="background-color: lightblue; padding: 16px;">
    <h2 style="color: black; text-align: center;"> PRICE PREDICTION USING ML BY CURIE </h2>
    
  
    
    """
    model = pickle.load(open('model.pkl','rb'))
    st.markdown(html_temp,unsafe_allow_html = True)
    
    st.write('')
    st.write('')
    
    st.markdown("##### ENTER THE PARAMETERS BELOW ")
    t1=st.number_input("OPEN PRICE", 0.00000,1000.0, step=1.00000)
    t2=st.number_input("HIGH ", 0.00000,10000.0, step=1.00000)
    t3=st.number_input("LOW", 0.00000,10000.0, step=1.00000)
    t4=st.number_input("AD CLOSE", 0.00000,10000.0, step=1.00000)
    
    
    data_new = pd.DataFrame({
        'Open':t1,
        'High':t2,
        'Low':t3,
        'Adj Close':t4,
        },index=[0])


    if st.button('pred'):
     with   st.spinner('LOADING...'):
        time.sleep(5)
        pred = model.predict(data_new)
     st.success("#### THE PREDICTED PRICE IS \n${} ".format(pred[0]))
     
if __name__== '__main__':
    main()
