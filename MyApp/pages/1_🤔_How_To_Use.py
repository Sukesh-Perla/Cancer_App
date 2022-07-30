import streamlit as st
import base64
st.set_page_config(
    page_title="How To Use",
    page_icon="🤔",
)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
    )

add_bg_from_url()
st.markdown('<h1 style="text-align:left;color:DeepPink;font-weight:bolder;font-size:40px;">How to Use the Application</h1>',unsafe_allow_html=True)


def load_gif():
    file_ = open("MyApp/Data/ezgif.com-gif-maker.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
        )

load_gif()

st.markdown('<h2 style="text-align:left;color:LightPink;">Instructions</h2>',unsafe_allow_html=True)
st.markdown('<h5 style="text-align:left;color:White;">Step 1: Go to the Predict tab, Fill the User Information.</h5>',unsafe_allow_html=True)
st.markdown('<h5 style="text-align:left;color:White;">Step 2: Upload The Image or Use the Sample Image.</h5>',unsafe_allow_html=True)
st.markdown('<h5 style="text-align:left;color:White;">Step 3: Click "Run On This Image" Button.</h5>',unsafe_allow_html=True)
st.markdown('<h5 style="text-align:left;color:White;">Step 3: Step 4: Predicted result will be displayed.</h5>',unsafe_allow_html=True)


st.write("#")
st.markdown('<h2 style="text-align:left;color:LightPink;">Who Can Use This App?</h2>',unsafe_allow_html=True)
st.markdown('#### Pathologists: They play a critical role in research, advancing medicine and devising new treatments to fight viruses, infections and diseases like cancer.')
st.markdown('#### Hospitals:    They can use the system as a tool to find the disease, time saving and fast.')
st.markdown('#### Patients:     Who have access to their pathology samples can run the system on their own.')

st.markdown('<h2 style="text-align:left;color:LightPink;">More Histopathology Images</h2>',unsafe_allow_html=True)
st.write("#### More histopathology Images are available at  [link](https://www.kaggle.com/datasets/ambarish/breakhis)")
