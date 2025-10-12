import streamlit as st
import pandas as pd
import plotly.express as px # Import plotly express


# Set Streamlit page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Scientific Visualization"
)

# Page header
st.header("Scientific Visualization", divider="grey")

# Load your data
try:
    df2 = pd.read_csv(
        'https://raw.githubusercontent.com/S23B0121-AqifAddin/tuto-SV/refs/heads/main/student_survey_exported%20(1).csv',
        encoding='utf-8'
    )
except UnicodeDecodeError:
    df2 = pd.read_csv(
        'https://raw.githubusercontent.com/S23B0121-AqifAddin/tuto-SV/refs/heads/main/student_survey_exported%20(1).csv',
        encoding='latin-1'
    )

# Filter Arts faculty if 'Faculty' column exists
arts_df = df2[df2['Faculty'] == 'Arts'] if 'Faculty' in df2.columns else df2

# Gender distribution chart using Plotly
if 'Gender' in arts_df.columns:
    st.subheader("Distribution of Gender in Arts Faculty (Plotly)")

    gender_counts = arts_df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']

    # Create a Plotly Pie Chart
    fig = px.pie(
        gender_counts,
        values='Count',
        names='Gender',
        title='Distribution of Gender in Arts Faculty',
        hole=0.3, # Optional: makes it a donut chart
        color_discrete_sequence=px.colors.qualitative.Pastel # Optional: sets a nice color theme
    )

    # Optional: Customize text info (e.g., show percentage and count on hover)
    fig.update_traces(textposition='inside', textinfo='percent+label')

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True) # Use st.plotly_chart

else:
    st.warning("The dataset does not contain a 'Gender' column.")
