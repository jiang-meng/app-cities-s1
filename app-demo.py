import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('Hello from Meng')
data = {
    'name': ['john','tom','mary'], 
    'gender' : ['male','male', 'female'],
    'age':[20, 22, 21],
}

# create plot
df = pd.DataFrame(data)
st.write(df)
st.write('this is a demo')

fig,ax = plt.subplots()
df.plot(ax=ax)
st.pyplot(fig)