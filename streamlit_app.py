import streamlit as st

st.title("Group Activity 3")
st.header("CSS145-BM4: Group 5")

st.subheader("Data Upload")
st.code("""
from google.colab import files
uploaded = files.upload()
""")

# Library Imports
st.subheader("Library Imports")
st.code("""
import squarify
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
""")

# Dataset Load
st.subheader("Dataset Load")
st.code("""
df = pd.read_csv('Electronic_sales_Sep2023-Sep2024.csv')
""")

# Tree Map: Gender
st.header("Tree Map: Gender")
st.code("""
def treemap_gender():
    gender_counts = df['Gender'].value_counts()
    squarify.plot(gender_counts, label=['Male', 'Female'],  color=['blue', 'pink'])
    plt.axis('off')
    plt.show()

treemap_gender()
""")

st.image("/workspaces/CSS145-BM4-Group5_Group-Activity-3/assets/treemap.png", caption="Tree Map: Gender", use_column_width=True)
st.text("The treemap chart compares both genders, showing little difference in product purchases.")