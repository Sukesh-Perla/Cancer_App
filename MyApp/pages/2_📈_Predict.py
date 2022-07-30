#Importing libraries
import streamlit as st
import base64
import datetime
import time
from PIL import Image
import numpy as np
import cv2
from opencv import cv2
from tensorflow.keras.models import load_model

st.set_page_config(
    page_title="Predict",
    page_icon="📈",
)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('MyApp/Bg.jpeg')



#Loading the model
cancer_model = load_model("Best_model/")

#make a title for your webapp
st.markdown('<h1 style="text-align:left;color:DeepPink;font-weight:bolder;font-size:40px;">User Information</h1>',unsafe_allow_html=True)
#Name
name = st.text_input('Enter Your Name')
#Age
age = st.number_input('Enter Your Age',format="%d",value=0)
#Gender
gender = st.selectbox('Select Your Gender',('select','Male', 'Female', 'Prefer Not To Say'))
#upload
uploaded_file = st.file_uploader("Choose an image...")
#Check box
agree = st.checkbox('Use Sample Image')

#Predict funtion
def pred(image_data):
    img = np.array(image_data)/255.
    img = np.resize(img,(128,128))
    img = np.expand_dims(img,axis=0)
    pred = (cancer_model.predict(img)>0.5).astype("int32").flatten()
    return pred

def info(pred):
    if pred == 0:
        st.markdown('<h4 style="text-align:left;color:Green;">The uploaded specimen has a very less chance of a Breast Cancer.</h4>',unsafe_allow_html=True)
        #Expander Box
        with st.expander("To know about precautionary measures, Please click on the links below",expanded = True):
            st.write("##### Understanding Breast Cancer -- Prevention - WebMD[link](https://www.webmd.com/breast-cancer/guide/understanding-breast-cancer-prevention)")
            st.write("##### Breast Cancer Risk and Prevention - American Cancer Society [link](https://www.cancer.org/cancer/breast-cancer/risk-and-prevention.html)")
            st.write("##### 8 Ways to prevent Breast Cancer - Siteman Cancer Center [link](https://siteman.wustl.edu/prevention/8-ways/8-ways-to-prevent-breast-cancer/)")

    else:
        st.markdown('<h4 style="text-align:left;color:Red;">The uploaded specimen has a very high chance of a breast cancer.</h4>',unsafe_allow_html=True)
        #Expander Box
        with st.expander("To know about what to do next, Please click on the links below", expanded = True):
            st.write("##### Breast cancer in women - Treatment - HSE.ie  [link](https://www2.hse.ie/conditions/breast-cancer-women/treatment/)")
            st.write("##### Breast cancer - Diagnosis and treatment - Mayo Clinic [link](https://www.mayoclinic.org/diseases-conditions/breast-cancer/diagnosis-treatment/drc-20352475)")
            st.write("##### If You Have Breast Cancer - American Cancer Society [link](https://www.cancer.org/cancer/breast-cancer/if-you-have-breast-cancer.html)")
            st.write("##### Living Beyond Breast Cancer - Ibbc.org [link](https://www.lbbc.org/blog/)")

#Agree button
if agree and uploaded_file is None:
    image_data = Image.open('benign_SOB_B_A-14-22549AB-200-013.png')
    st.image(image_data.resize((512,256)))

else:
    if uploaded_file is not None:
        image_data = Image.open(uploaded_file)
        st.image(image_data.resize((512,256)))

#Prediction on clicking Run Button
result = st.button('Run On This Image')
if result:
    with st.spinner('Wait for it...'):
        time.sleep(1)
        class_pred = pred(image_data)
        info(class_pred)
