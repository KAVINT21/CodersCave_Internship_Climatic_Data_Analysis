import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv("D:\Internships\CodersCave\weather.csv")

# Sidebar with city selection
selected_city = st.sidebar.selectbox("Select City", df['city'].unique())

# Filter data based on selected city
city_data = df[df['city'] == selected_city]

# Plot 1: Line chart for Temperature Trends
st.subheader("Temperature Trends Over Time")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.lineplot(x='time', y='tavg', data=city_data[:1000], label='Average Temperature', ax=ax1)
sns.lineplot(x='time', y='tmin', data=city_data[:1000], label='Min Temperature', ax=ax1)
sns.lineplot(x='time', y='tmax', data=city_data[:1000], label='Max Temperature', ax=ax1)
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Temperature Trends Over Time")
st.pyplot(fig1)





# Plot 6: Pair plot for selected numerical columns
st.subheader("Pair Plot for Numerical Columns")
num_cols = ['tavg', 'tmin', 'tmax', 'prcp']
fig6 = sns.pairplot(city_data[num_cols])
st.pyplot(fig6)

# Plot 7: Correlation heatmap
st.subheader("Correlation Heatmap")
fig7, ax7 = plt.subplots(figsize=(8, 6))
corr_matrix = city_data[num_cols][:3].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax7)
plt.title("Correlation Heatmap")
st.pyplot(fig7)



# Plot 8: Distribution of Temperature
st.subheader("Distribution of Temperature")
fig8, ax8 = plt.subplots(figsize=(8, 6))
sns.kdeplot(data=city_data, x='tavg', fill=True, ax=ax8)
sns.kdeplot(data=city_data, x='tmin', fill=True, ax=ax8)
sns.kdeplot(data=city_data, x='tmax', fill=True, ax=ax8)
plt.xlabel("Temperature")
plt.title("Distribution of Temperature")
st.pyplot(fig8)





# Create a Streamlit figure
fig, ax = plt.subplots(figsize=(15, 8))
sns.set_style(style='darkgrid')
sns.violinplot(data=city_data, x='city', y='tmin', alpha=.01, ax=ax)
sns.violinplot(data=city_data, x='city', y='tmax', ax=ax)
ax.set_ylabel('Temperature')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_title('Daily Min and Max Temperature Distribution by Cities', fontsize=15)

# Display the plot in Streamlit
st.pyplot(fig)