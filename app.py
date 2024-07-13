import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import plotly.express as px

# Load the model
model = joblib.load('best_model.pkl')

# Load the cleaned and balanced dataset with lat and long
df = pd.read_csv('cleaned_data_with_lat_long.csv')

# Streamlit app
st.title("Credit Card Transactions Dashboard")

# Display the number of frauds in the selected category
category = st.selectbox("Select a category of fraud", df['category'].unique())
st.write("Number of frauds in selected category:", len(df[df['category'] == category]))

# Prediction form
st.header("Predict Fraud")
amount = st.number_input("Amount")
gender = st.selectbox("Gender", df['gender'].unique())
state = st.selectbox("State", df['state'].unique())
hour = st.selectbox("Hour", df['hour'].unique())

if st.button("Predict Fraud"):
    input_data = pd.DataFrame({
        'amount': [amount],
        'gender': [gender],
        'state': [state],
        'hour': [hour],
        'category': [category]
    })
    
    # Scale the input data
    scaler = StandardScaler()
    scaler.fit(df.drop(columns=['is_fraud']))
    input_data_scaled = scaler.transform(input_data)
    
    # Predict using the loaded model
    prediction = model.predict(input_data_scaled)
    
    # Display the prediction
    st.write("Fraud Prediction:", "Fraud" if prediction[0] == 1 else "Not Fraud")

# Map visualization
st.header("Fraud across locations")
if st.checkbox("Show Map"):
    fig = px.scatter_mapbox(
        df, lat="lat", lon="long", color="is_fraud", size="amount",
        color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10
    )
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig)

# Bar chart visualization
st.header("Fraud Transactions by Category")
if st.checkbox("Show Bar Chart"):
    category_count = df['category'].value_counts()
    fig = px.bar(category_count, x=category_count.index, y=category_count.values, labels={'x': 'Category', 'y': 'Count'})
    st.plotly_chart(fig)
