import streamlit as st

st.title('welcome to Bar-Island')
st.write('here you can brew your drink as per your wish')

a = st.checkbox('You Are Adult  ? ')
if a:
    st.success('you may proceed')


b=st.button('Would you like to customize your drink ! ')
if b:
    st.write('okk.. your wish is our command')


n=st.text_input("Enter Your Name",key='Name')
if n:
    st.write(f"Welcome {n}")

dob=st.date_input("Enter Your Order date",key="DOB")
if dob:
    st.write(f"your order data {dob}")


order=st.number_input('How Many Order Would You Like To Place',min_value=1,max_value=10,step=1)
st.success(f"Your {order} Your Order OTW")

y_base=st.radio('Select Your Base ',["Sparking Water","Fruit=Juice","Wine","Gin","Beer","Alcohol"])
st.write(f"selected {y_base} as a Base")

flavour=st.selectbox('Choose Flavour',["chocolate","Mango","Strawberry","Mint","Plain"])
st.write(f'{flavour}........Great Choice')

drink_size=st.slider('Drink Size',0,90,30)
st.success('Your Drink Size Is {y_base}...ML')

