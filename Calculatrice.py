import streamlit as st
st.title("Welcome to Python Pizza Deliveries")
size = st.text_input("what size do you want? small, medium, large")
add_peperoni = st.text_input("do you want peperoni? YES or NO")
extra_cheese = st.text_input("do you want extra_cheese? YES or NO")

prix = 0

if size == "small":
    prix=3000
elif size == "medium":
    prix=4000
elif size == "large":
    prix=5000

if add_peperoni == "YES":
    if size == "small":
        prix +=1000
    else:
        prix +=1500

if extra_cheese == "YES":
    prix +=1500

print(f"VOTRE FACTURE FINALE EST DE:{prix}FCFA")

st.button('TOTAL')
st.write(f"VOTRE FACTURE FINALE EST DE:{prix}FCFA")
