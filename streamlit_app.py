import streamlit as st
import google.generativeai as genai
from PIL import Image


choice=st.selectbox('select your choice',['choose','Temperature Converter','Image Analytics','chat app'])
if(choice=='Temperature Converter'):
    st.title('Temperature converter')
    Temperature=st.number_input('Enter Temperature:')
    convert=st.selectbox('select conversion',['Celsius','Farhneite'])
    if st.button('Convert'):
        if(convert=='Celsius'):
            result=(5/9)*(Temperature-32)
        else:
            result=(Temperature*(9/5))+32
        st.success('Converted Temperature is {} {}'.format(round(result,2),convert))
elif(choice=='Image Analytics'):
  
    api_key="AIzaSyBUUejpbU_3eouCT96lkHmkE2mQ6jQb8TU"
    genai.configure(api_key=api_key)

    st.header("Image analytics")

   
    uploaded_file=st.file_uploader("Upload an image",type=["png","jpg","jpeg"])

    if uploaded_file is not None:
        st.image(Image.open(uploaded_file))

    ############ What you want ask ####################
    prompt=st.text_input("Enter the text")

    ######### Use genai skill ##########################

    if st.button("GET RESPONSE"):
        img=Image.open(uploaded_file)
        model=genai.GenerativeModel("gemini-1.0-pro-vision-latest")
        response=model.generate_content([prompt,img])
        st.markdown(response.text)
elif(choice=='chat app'):
    api_key="AIzaSyBUUejpbU_3eouCT96lkHmkE2mQ6jQb8TU"
    genai.configure(api_key=api_key)

    st.header("Chat app")

    prompt=st.text_input("Enter the text")

    if st.button("GET RESPONSE"):
        model=genai.GenerativeModel("gemini-pro")
        response=model.generate_content([prompt])
        st.markdown(response.text)

