import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

df=pd.read_csv('iris.csv')
st.write(df)

st.sidebar.header("Pick two variables for scatter variables")

x=st.sidebar.selectbox('Pick your x_axis',df.select_dtypes(include=np.number).columns.tolist())
y=st.sidebar.selectbox('Pick your y_axis',df.select_dtypes(include=np.number).columns.tolist())




scatter=alt.Chart(df, title=f"Correlation between {x} and {y}"). mark_point().encode(
alt.X(x,title=f"{x}"),
alt.Y(y,title=f"{y}"),
tooltip=[x,y])
st.altair_chart(scatter, use_container_width=True)

corr= round(df[x].corr(df[y]),2)

st.write(f"The Correlation between {x} and {y} is {corr} ")