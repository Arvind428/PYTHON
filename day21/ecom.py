import streamlit as st
#Page Config
st.set_page_config(layout="wide")

#Sample products
products=[
    {
        "name":"Python Basics",
        "price":500,
        "image":"1.jpg"
    },
    {
        "name":"Data Science",
                "price":987,
        "image":"Symbiote Spider-Man.jpg"
    
    },
    {
        "name":"AI Fundamentals",
        "price":1000,
        "image":"Spiderman.jpg"
    }
]

#Initialize cart
if "cart" not in st.session_state:
    st.session_state.cart=[]

#Layout:Left (products) + Right (cart)
col1,col2=st.columns([3,1])

#----------------------LEFT SIDE (PRODUCTS)---------------------------------------
with col1:
    st.title("Book Store")

    for i,product in enumerate(products):
        st.image(product["image"],width=150)
        st.subheader(product["name"])
        st.write(f"Price:${product['price']}")

        if st.button(f"Add to Cart (i)"):
            st.session_state.cart.append(product)

        st.markdown("----")

#----------------RIGHT SIDE (CART)-------------
with col2:
    st.title("Cart")

    total=0

    if len(st.session_state.cart)==0:
        st.write("Cart is empty")
    else:
        for item in st.session_state.cart:
            st.write(f"{item['name']}-${item['price']}")