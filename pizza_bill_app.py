import streamlit as st

st.title("🍕 Pizza Bill Generator")

pizza_size = st.selectbox("Pick a size", ["S", "M", "L"])
pepperoni = st.radio("Do you want pepperoni?", ["Yes", "No"])
cheese = st.radio("Do you want extra cheese?", ["Yes", "No"])

# Your logic stays almost the same
bill = 0
if pizza_size == "S": bill = 15
elif pizza_size == "M": bill = 20
elif pizza_size == "L": bill = 25

if pepperoni == "Yes":
    bill += 2 if pizza_size == "S" else 3
if cheese == "Yes":
    bill += 1

st.success(f"Your Total Bill: {bill} INR")