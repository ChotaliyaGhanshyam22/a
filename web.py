import streamlit as st 
st.title('Welcome To My Bar Island')

st.write('We Are Introducing To New Drinks In House .\n do vote tour few')

cl1,cl2=st.columns(2)
with cl1:
    st.subheader('Assam Tea')
    st.image("https://blog.swiggy.com/wp-content/uploads/2025/02/Image-1_-1-2-1024x538.webp",width=200)
    v1=st.button('Vote For Assam Tea')



with cl2:
    st.subheader('Mango Boba Tea')
    st.image("https://www.1mg.com/articles/wp-content/uploads/2024/07/3341.jpg",width=200)
    v2=st.button('Vote For Mango Boba Tea Tea')


if v1:
    st.success('You Have Voted Asaam Tea')

if v2:
    st.success('You Have Voted Mango Boba Tea Tea')

st.sidebar.subheader('Customize Your Drink')
st.sidebar.write('Tell Us About You & Your Drink..')
n=st.sidebar.text_input("Your_Name")
c=st.sidebar.selectbox('Select Your Base',['Almond Milk','Water','Coconut Milk'])
a=st.sidebar.slider('Sugar Level In Spoon',0,5,1)
st.sidebar.success(f'You Want {a} Spoon Of Sugar')

b=st.sidebar.checkbox('Would You Like To Add Cinamon')
if b:
    st.sidebar.success('Adding Cinemon')
    st.sidebar.balloons()
st.write(f"Welcome {n}! You Have Ordered Tea with {c} as a base containing {a} tea spoon sugar")
