import streamlit as st
import langchain_data
st.title("Resturant Name Generator")
cuisine=st.sidebar.selectbox("Pick a Cuisine",("Indian","Italian","Mexican","Arabic","American","chinese"))


if cuisine:
    response=langchain_data.generate_name(cuisine)
    st.header(response['resturant_name'].strip())
    food_items=response['food_items'].strip().split(",")
    for item in food_items:
        st.write("-",item)
