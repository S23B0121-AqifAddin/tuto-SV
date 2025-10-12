import matplotlib.pyplot as plt

gender_counts = arts_df['Gender'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Gender in Arts Faculty')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
