import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Title for the web app
st.title("Student Survey Data Viewer")

# Try reading the CSV file with different encodings
try:
    df2 = pd.read_csv('https://raw.githubusercontent.com/S23B0121-AqifAddin/tuto-SV/refs/heads/main/student_survey_exported%20(1).csv', encoding='utf-8')
except UnicodeDecodeError:
    df2 = pd.read_csv('https://raw.githubusercontent.com/S23B0121-AqifAddin/tuto-SV/refs/heads/main/student_survey_exported%20(1).csv', encoding='latin-1')

# Show a preview of the dataset
st.subheader("Preview of the Dataset")
st.dataframe(df2.head())  # Interactive table

# Optionally, show summary info
st.subheader("Dataset Information")
st.write(f"Rows: {df2.shape[0]}, Columns: {df2.shape[1]}")

# Optionally, let user select columns to view
columns = st.multiselect("Select columns to view:", df2.columns)
if columns:
    st.dataframe(df2[columns])

gender_counts = arts_df['Gender'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Gender in Arts Faculty')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
