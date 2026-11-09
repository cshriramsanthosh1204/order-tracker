import requests
import streamlit as st

API_BASE = "http://127.0.0.1:8000"

st.title("Track your order")
st.write("Enter your order number (try BT1042)")

order_id = st.text_input("Order number", placeholder="e.g. BT1042")


def show_result(order):
    st.success(f"{order['item']} is: {order['status']}")


def show_error(message):
    st.error(message)


if st.button("Track"):
    order_id = order_id.strip()
    if order_id == "":
        st.warning("Please enter an order number.")
    else:
        response = requests.get(f"{API_BASE}/orders/{order_id}", timeout=5)

        if response.status_code == 200:
            order = response.json()
            show_result(order)
        else:
            show_error("Order not found.")