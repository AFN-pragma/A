import streamlit as st
st.title("Welcome to Python Pizza Deliveries")
size = st.text_input("what size do you want? small, medium, large")
add_peperoni = st.text_input("do you want peperoni? YES or NO")
extra_cheese = st.text_input("do you want extra_cheese? YES or NO")

prix = 0

if size == "small":
    prix=15
elif size == "medium":
    prix=20
elif size == "large":
    prix=25

if add_peperoni == "YES":
    if size == "small":
        prix +=2
    else:
        prix +=3

if extra_cheese == "YES":
    prix +=1

print(f"VOTRE FACTURE FINALE EST DE:{prix}FCFA")

st.button('TOTAL')
st.write(f"VOTRE FACTURE FINALE EST DE:{prix}FCFA")
