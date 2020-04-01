#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

visualize = st.cache(pd.read_csv)('Recommendation_1.csv')
visualize2= visualize.drop(['Unnamed: 0'],axis=1)

data = st.cache(pd.read_csv)('dataSubset5000_take2.csv')
df = st.cache(pd.read_csv)('Item_list.csv')
#df= pd.read_csv(r'C:\Users\prafu\Item_list.csv')
df=df.reset_index()
df.rename(columns={'index': 'itemID'}, inplace=True)

data_all=data.merge(df, on='itemID', how='left')


def show_about():
        ''' Home / About page '''
        st.title('Recommendation systems using SVM')
        my_slot1 = st.empty()
        # Appends an empty slot to the app. We'll use this later.

        my_slot2 = st.empty()
        # Appends another empty slot.

        st.write('SAR is a fast, scalable, adaptive algorithm for personalized recommendations based on user transaction history.It is   powered by understanding the similarity between items, and recommending similar items to those a user has an existing affinity for.')
        # Appends some more text to the app.
        
        st.header('How the Algorithm helps Snackfair?')
        my_slot2 = st.empty()
        my_slot2 = st.empty()
        st.write('SAR Algorithm provides 2 kinds of recommendations:')
        st.subheader('User recommendations:')
        my_slot2 = st.empty()
        st.write('which recommend items to individual users based on their transaction history')
        my_slot2 = st.empty()
        st.subheader('Frequently-Occurring-Together recommendations:')
        st.write('which recommend items similar to a given set of items')



def Recommendation_model():
    st.title('Personalized Snack Recommendations')
    st.subheader('You might also like these:')
    variables = st.sidebar.multiselect("Enter the User ID to get top 10 recommendations", visualize2['userID'].unique())
    


    two_clubs_data = visualize2[(visualize2['userID'].isin(variables))]
    data_all_variable = data_all[(data_all['userID'].isin(variables))]
    club_data_is_check = st.checkbox("Recommendations for the selected User ID")
    if club_data_is_check:
        st.write(two_clubs_data[['Item','Category','Taste','Health Meter']])
    st.subheader('Customer previously bought:')
    His_check = st.checkbox("Products bought by the selected User ID")
    if His_check:
        st.write(data_all_variable[['Item','Category','Taste','Health Meter']])
        
        
        
def explore_analytics():
    st.title('Customer Portfolio and Statistics')
    if st.button("Column Names"):
          st.write(data_all.columns)
    
    # Select Columns
    if st.checkbox("Select All Data To Show"):
        all_columns = data_all.columns.tolist()
        selected_columns = st.multiselect("Select",all_columns)
        new_df = data_all[selected_columns]
        st.dataframe(new_df.head())
    
    #values = st.sidebar.slider(f"productRating range", float(data_all.productRating.min()), 1000., (50., 300.))
    #f = px.histogram(data_all.query("productRating.between{values}"), x="productRating", nbins=15, title="productRating distribution")
    #f.update_xaxes(title="productRating")
    #f.update_yaxes(title="No. of listings")
    #st.plotly_chart(f)'''
    


    hm = st.sidebar.multiselect('What kind of food you like?', df['Health Meter'].unique())
    category = st.sidebar.multiselect('Which Category do you like the best?', data_all['Category'].unique())

    #taste = st.multiselect('Select your fav taste?', data_all['Taste'].unique())   
    #hm = st.multiselect('Which Category do you like the best?',df['Health Meter'].unique())
    #x = st.slider('x')
    new_df = data_all[
        (data_all['Category'].isin(category)) 
        & (data_all['Health Meter'].isin(hm)) ]#&   (data_all['Taste'].isin(taste))]
    st.write('You selected:', new_df)
    if st.checkbox("Scatter Plot To Show"):
        fig = px.scatter(new_df['productRating'], x ='productRating')
        st.plotly_chart(fig)
    
            

            
            
st.sidebar.title("Explore")
app_mode = st.sidebar.selectbox( "Choose an Action", [
"About",
"Analytics",
"Recommendation"
])



# nav
if   app_mode == "About":              show_about()
elif app_mode == "Analytics":          explore_analytics()
elif app_mode == 'Recommendation':     Recommendation_model()
    


            



