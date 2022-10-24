import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('World Cities')
df = pd.read_csv('worldcities.csv')

#add a slider
pop_slider = st.sidebar.slider('Choose a population',0.0,40.0,3.6)
df = df[df.population >= pop_slider]

# create a multi select
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  # options
     df.capital.unique()) # defaults

# capital_filter is a list of users choices

# create a input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")

# filter by country
df = df[df.capital.isin(capital_filter)]

if country_filter!='ALL':
    df = df[df.country == country_filter]

#filter by population

df = df[df.capital.isin(capital_filter)]

#show on map (dataframe should contain 经纬度 )
st.map(df)

# show df
st.write(df)

# show the pop plot
pop_sum = df.groupby('country')['population'].sum()
fig,ax = plt.subplots()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)