#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import streamlit as st
import numpy as np

visualize = st.cache(pd.read_csv)('Recommendation_1.csv')
visualize2= visualize.drop(['Unnamed: 0'],axis=1)


is_check = st.checkbox('Display Data')
if is_check:
 st.write(visualize2)

variables = st.sidebar.multiselect('Enter the variables', visualize2.columns)
st.write('You selected these variables', variables)

#selectedUserID= st.selectbox("Choose your UserID: ", np.arange(0, 999, 1))
selectedItemID = st.selectbox("Choose your ItemID:" , np.arange(0,50,1))
selectedItem =  st.multiselect("Select an Item",["Kurkure","Uncle chips","Milano Dark Chocolate","Bournville Dark Chocolate",
"Chips Ahoy Chunky","Miranda","Pepsi","Fanta","Cococola","Hersheys Kisses","Hersheys Nuggets","Tootsie Pops","Smarties",
"Limca","Mountain Dew","Haldirams Aloo Bhujia","Haldirams Fried Peanuts","Rajaram Peanut Candy","Bharath Chikki",
"Lilys Brownie Fudge","Lilys Tart Cookies","Cadburys Diarymilk","Bournvita","Boost","Horlicks","Maltova","Milo",
"Maple Syrup","Haldirams Khatta Meeta","Haldirams Bhel Puri","Keebler Chips Deluxe","Nature Valley Protien Bar",
"Quaker Chewy","Kind Health Grains","Kudos Bars","Viva","Manna Health Mix","Modern Bread","Wonder Cake","Betty Croker Super Moist Cake",
"Pillsbury Vanilla Cake","Hostess Twinkies","Kuppies Orange Cake","Parle-G","Brittania Bourbon","Brittania Marie Gold",
"Sunfeast Dark Fantasy","Brittania Little Hearts","Ragu Pasta Sauce","Britannia 50-50"])
healthoption =  st.multiselect("What is the required health option?",["Healthy", "Junk Food"])
taste =  st.multiselect("Select a taste",["Sweet", "Spicy"])

#userID_is_check = st.checkbox('Display the data of selected IDs')
#if userID_is_check:
 #st.write(selectedUserID)

itemID_is_check = st.checkbox('Display the data of selected IDs')
if itemID_is_check:
 st.write(selectedItemID)

item_check = st.checkbox('Display the data of selected Items')
if item_check:
 st.write(selectedItem)

health_check = st.checkbox('Display the data of selected health option')
if health_check:
 st.write(healthoption)

taste_check =st.checkbox('Display the data of selected taste option')
if taste_check:
 st.write(taste)


# In[52]:


import matplotlib.pyplot as plt
import seaborn as sns
color = sns.cubehelix_palette(10, start=2, rot=0, dark=0.2, light=0.8, reverse=True)
#%matplotlib inline


# In[53]:


visualize2.head()


# In[64]:


def get_value_count_and_plot(data, title, limit=20):
    value_count = visualize2.itemID.value_counts()[:limit]
    item_id = value_count.index.values
    prod_names = visualize2[visualize2.itemID.isin(item_id)].Item

    sns.set(font_scale=1)
    sns.barplot(y=prod_names, x=value_count.values, orient='h', palette=color)
    plt.figure(figsize=(40,80))
    plt.suptitle(title)
    plt.show()
   # st.pyplot()

    
title =" Top Products in Overall"
get_value_count_and_plot(visualize, title)


# In[65]:


st.pyplot()

