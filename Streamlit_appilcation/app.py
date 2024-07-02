import streamlit as st

# Configure the app
st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="🏡",
)

# Title and introduction
st.title("Real Estate Price Prediction, Analysis, and Recommendation System")
st.write("""
Welcome to the Real Estate Price Prediction, Analysis, and Recommendation System. 
Use this app to predict house prices, analyze real estate trends, and get recommendations based on various parameters.
""")
st.image(r"picture\Untitled design.png", caption="Explore Real Estate Trends", use_column_width=True)
# Sidebar navigation

# Home page content
st.header("Home")
st.write("""
This is the home page of the Real Estate Price Prediction, Analysis, and Recommendation System.

You can navigate to different sections using the sidebar:
- **Price Prediction**: Predict the price of a house based on input features.
- **Analysis**: Analyze different areas.
- **Recommendations**: Get recommendations for buying properties.
""")




st.subheader("Get Started")
st.write("Use the sidebar to navigate through different features of the app. Here’s a quick overview of what you can do:")

st.markdown("""
- **Price Prediction**: Input details such as the number of bedrooms, bathrooms, square footage, and location to predict the price of a house.
- **Market Analysis**: View and analyze real estate market trends with charts and statistics.
- **Recommendations**: Get personalized recommendations for buying properties based on your preferences and market conditions.
""")

st.subheader("Why Use This App?")
st.write("""
This app provides a comprehensive suite of tools for anyone interested in real estate, whether you're a buyer, seller, or investor. 
- **Accurate Predictions**: Leverage advanced algorithms to predict property prices.
- **In-Depth Analysis**: Gain insights into market trends and make informed decisions.
- **Personalized Recommendations**: Receive tailored advice based on your specific needs and market data.
""")

st.info("Navigate to the Price Prediction section to get started with predicting house prices!")

# Footer
st.sidebar.write("""
---
Created by [Nikhil kumar]
""")
