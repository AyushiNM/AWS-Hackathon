import streamlit as st 
import infer
st.title('AWS Disaster Response Hackathon')
st.sidebar.image('earthquake.jpg')
selection = st.sidebar.selectbox(
    "what are you searching for?",
    ("","Earthquake Information", "Estimate Food and shelter items", "Earthquake News")
)

# selection = st.sidebar.selectbox("Go to page:", [ "Earthquake Information", "Estimate Food and shelter items", "Earthquake News"])
if selection == 'Earthquake Information':
    st.title('Earthquake Information')
    st.write(infer.predict())
elif selection == 'Estimate Food and shelter items':
    st.title('Estimate Food and shelter items')
elif selection == 'Earthquake News':
    st.title('Earthquake News')
else:
    st.title('Main Page')
