import streamlit as st
import numpy as np
from PIL import Image

from tensorflow import keras
import tensorflow as tf
from keras import layers
from tempfile import NamedTemporaryFile
from keras.preprocessing.image import load_img

   
   


# main title 
st.title('Dermothologist Ai')
st.markdown("\n")

image = Image.open("assets/Images/Main.png")
st.image(image, caption= 'Simple Example what we are looking into',  use_column_width=True)

st.title('Model will be soon uploaded')