import streamlit as st
import pandas as pd
import plotly.express as px # Import plotly express
import plotly.express as plt

# Set Streamlit page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Tutorial Scientific Visualization"
)

# Page header
st.header("Tutorial Scientific Visualization", divider="grey")

# Load your data
try:
  df2 = pd.read_csv('https://raw.githubusercontent.com/S23B0121-AqifAddin/tuto-SV/refs/heads/main/student_survey_exported%20(1).csv', encoding='utf-8')
except UnicodeDecodeError:
  df2 = pd.read_csv('https://raw.githubusercontent.com/S23B0121-AqifAddin/tuto-SV/refs/heads/main/student_survey_exported%20(1).csv', encoding='latin-1')

df2

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

academic_year_counts = arts_df['Masters Academic Year in EU'].value_counts().reset_index()
academic_year_counts.columns = ['Masters Academic Year in EU', 'Count']

plt.figure(figsize=(10, 6))
sns.barplot(x='Masters Academic Year in EU', y='Count', data=academic_year_counts, palette='viridis')
plt.title('Distribution of Academic Year in Arts Faculty')
plt.xlabel('Academic Year')
plt.ylabel('Number of Students')
plt.show()


plt.figure(figsize=(8, 6))
plt.scatter(arts_df['Q3 [What was your expectation about the University as related to quality of resources?]'],
            arts_df['Q5 [To what extent your expectation was met?]'])
plt.title('Expectation vs. Met Expectation for Quality of Resources (Arts Faculty)')
plt.xlabel('Expectation about Quality of Resources')
plt.ylabel('Extent Expectation Met')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(y='Q7. In your opinion,the best aspect of the program is', data=arts_df, palette='viridis', order = arts_df['Q7. In your opinion,the best aspect of the program is'].value_counts().index)
plt.title('Distribution of Best Aspects of the Program (Arts Faculty)')
plt.xlabel('Count')
plt.ylabel('Best Aspect of the Program')
plt.show()

plt.figure(figsize=(12, 8))
sns.countplot(y='What aspects of the program could be improved?', data=arts_df, palette='viridis', order = arts_df['What aspects of the program could be improved?'].value_counts().index)
plt.title('Aspects of the Program that Could be Improved (Arts Faculty)')
plt.xlabel('Count')
plt.ylabel('Aspects for Improvement')
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(x='Do you feel that the quality of education improved at EU over the last year?', data=arts_df, palette='viridis')
plt.title('Perceived Improvement in Education Quality (Arts Faculty)')
plt.xlabel('Response')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8, 6))
sns.countplot(x='Do you feel that the image of the University improved over the last year?', data=arts_df, palette='viridis')
plt.title('Perceived Improvement in University Image (Arts Faculty)')
plt.xlabel('Response')
plt.ylabel('Count')
plt.show()
