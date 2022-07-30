import streamlit as st
import base64
import pandas as pd
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Welcome",
    page_icon="🙏🏼",
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

st.markdown('<h1 style="text-align:center;color:DeepPink;font-weight:bolder;font-size:40px;">BREAST CANCER DETECTION SYSTEM</h1>',unsafe_allow_html=True)
st.write("#")
st.markdown('<div style="text-align:center"><img src="https://www.cubaheal-caribbean.com/wp-content/uploads/2020/01/breast-cancer-1.png"alt="Image Not found" width="500" height="300"/></div>',unsafe_allow_html=True)
#Intro
st.markdown('<h2 style="text-align:center;color:LightPink;">What is Breast Cancer?</h2>',unsafe_allow_html=True)
st.markdown('#### Breast cancer is a disease in which malignant (cancer) cells form in the tissues of the breast. Different types of breast cancer exists. The 2 main groups are non-invasive breast cancers and invasive breast cancers.')

#Facts
st.write("#")
st.markdown('<div style="text-align:center"><img src="https://b-bakery.com/images/imported/Breast-cancer-facts-Infographic.jpg"alt="Image Not found" width="400" height="550"/></div>',unsafe_allow_html=True)
st.write("#")
st.write("##### There's a good chance of recovery if it's detected at an early stage.")
#Causes
st.markdown('<h2 style="text-align:center;color:LightPink;">What Causes Breast Cancer?</h2>',unsafe_allow_html=True)

#symptoms
st.write("#")
st.markdown('<div style="text-align:center"><img src="https://www.verywellhealth.com/thmb/T8-5oQl-_nwAsPLUnZJ92mNX1z8=/614x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/breast-cancer-causes-513575-FINAL-d3477fdbdf1e404290ce7cf86038c769.jpg" alt="Image Not found" width="614" height="409"/></div>',unsafe_allow_html=True)
st.write("#")
st.markdown('<h2 style="text-align:center;color:LightPink;">How To Detect Breast Cancer?</h2>',unsafe_allow_html=True)
st.markdown('#### Your healthcare provider will perform a breast examination and ask about your series of family, medical history and any existing symptoms. Your healthcare provider will also recommend tests to check for breast abnormalities. These tests may include')
st.write("##### __BREAST ULTRASOUND__, __DIAGNOSTIC MAMMOGRAM__, __BREAST MAGNETIC RESONANCE IMAGE (MRI)__, __BIOPSY__.")

st.markdown('<div style="text-align:center"><img src="https://www.playtimes.com.hk/wp-content/uploads/2020/10/rsz_shutterstock_1803793069.jpg"alt="Image Not found" width="667" height="352"/></div>',unsafe_allow_html=True)
st.write("#")
# Find
st.markdown('<h2 style="text-align:center;color:LightPink;">Know The Breast Cancer Treatment Centres</h2>',unsafe_allow_html=True)
st.markdown('#### Select your Country:')


@st.cache
def getdata(file_csv):
    df = pd.read_csv(file_csv,encoding= 'unicode_escape')
    return df

def getcountry(df):
    return sorted(df['Country'].unique())

def getcentre(country,df):
    df=df[df['Country'] == country]
    df=df[["No.","Centres","Town"]]
    return df

def gettype(data):
    return type(data)
#get data
data=getdata("MyApp/data.csv")

#st.write(datadata.set_index('Country'))
country = getcountry(data)
Host_Country = st.selectbox('',country)

centres=getcentre(Host_Country,data)
st.write(centres.set_index('No.'))
