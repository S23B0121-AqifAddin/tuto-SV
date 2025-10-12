import streamlit as st 

  st.set_page_config(
    page_title="Scientific Visualization"
  )

  st.header("Scientific Visualization", divider="grey")
import pandas as pd
import matplotlib.pyplot as plt

# Load your data
try:
    df2 = pd.read_csv('https://raw.githubusercontent.com/S23B0121-AqifAddin/tuto-SV/refs/heads/main/student_survey_exported%20(1).csv', encoding='utf-8')
except UnicodeDecodeError:
    df2 = pd.read_csv('https://raw.githubusercontent.com/S23B0121-AqifAddin/tuto-SV/refs/heads/main/student_survey_exported%20(1).csv', encoding='latin-1')

# If you have an arts_df filtered version
arts_df = df2[df2['Faculty'] == 'Arts'] if 'Faculty' in df2.columns else df2

# Count gender
if 'Gender' in arts_df.columns:
    gender_counts = arts_df['Gender'].value_counts()

    # Create a figure
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
    ax.set_title('Distribution of Gender in Arts Faculty')
    ax.axis('equal')  # Circle shape

    # Display in Streamlit
    st.pyplot(fig)
else:
    st.warning("The dataset does not contain a 'Gender' column.")
