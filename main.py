import streamlit as st 
import infer

def main():
    st.title('AWS Disaster Response Hackathon')
    st.sidebar.image('earthquake.jpg')
    selection = st.sidebar.selectbox(
        "what are you searching for?",
        ("","Earthquake Information", "Estimate Food and shelter items", "Earthquake News")
    )

    # selection = st.sidebar.selectbox("Go to page:", [ "Earthquake Information", "Estimate Food and shelter items", "Earthquake News"])
    if selection == 'Earthquake Information':
        st.title('Earthquake Information')
    elif selection == 'Estimate Food and shelter items':
        st.title('Estimate Food and shelter items')
    elif selection == 'Earthquake News':
        st.title('Earthquake News')
    else:
        st.title('Main Page')
        with st.expander("Earthquake Assistance"):
            input = st.text_input("Type your query here - ", value="", key = 1)
            if  input != "":
                output = infer.predict(input, "earthquake")
                st.write(output)
        with st.expander("First Aid Assistance"):
            input = st.text_input("Type your query here - ", value="", key = 2)
            if  input != "":
                output = infer.predict(input, "firstaid")
                st.write(output)

if __name__ == '__main__':
    main()
