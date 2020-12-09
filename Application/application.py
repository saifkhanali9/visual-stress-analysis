import pandas as pd
import streamlit as st
import time
import numpy as np
import random
import plotly.express as px
from PIL import Image
from PIL import ImageFilter
imageLocation = st.empty()
images = np.arange(1, 16)
with open(r"C:\Users\Lars\Documents\BCI-Seminar\bison_not_seminar\Application\cssTemplate.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
while True:
    randomImage = random.choice(images)
    originalImage = Image.open(
        r'C:\Users\Lars\Documents\BCI-Seminar\bison_not_seminar\Application\Images\\' + str(
            randomImage) + '.PNG')
    blurredImage = originalImage.filter(ImageFilter.GaussianBlur(radius=2.9))
    # st.title('BCI Application')
    imageLocation.image(originalImage, width = 1000)
    # st.image(im1, width=1000)
    time.sleep(4)
    imageLocation.image(blurredImage, width = 1000)
    time.sleep(4)
    # time.sleep(10000)
    # im1 = image.filter(ImageFilter.BLUR)
    # st.image(im1)
