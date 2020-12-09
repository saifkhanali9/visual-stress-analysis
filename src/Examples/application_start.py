import sys
import threading
import mne
import os
mne.set_log_level('WARNING')

sys.path.insert(0, r'C:\Users\BCI-Seminar\Documents\visual_stress_do_not_open\bison_not_seminar')
from PIL import Image
import streamlit as st
from PIL import ImageFilter
import numpy as np
import time
from src import Unicorn_Recorder
from src.Unicorn_Recorder.Dummies import SawTooth
from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
import random
import pickle
from keras.models import load_model


#reserve the image location for the later application
imageLocation = st.empty()

feedbackLocation = st.empty()

#make the start button
start_button = st.button('Start!')
#set up a checkbox to hide the options
agree = st.checkbox('Check to setup Blurriness level (uncheck before pressing start)')

#initialize an array of random numbers to pick a random image later on
images = np.arange(1, 16)
global imageCondition
imageCondition = 'Not Blurred'
#predictedImageCondition = 0

if not start_button and agree:
    #set the title
    title = st.title('Set your preferences!')

    #set the description
    st.write('Choose a radius for a Gaussian-Blur filter:')

# Show an example number and choose blurriness on the slider
slider_position = st.empty()
slider = slider_position.slider('', 0.0, 4.0)

#show example image for the amount of blurriness chosen by the slider
if not start_button and agree:
    example_number = Image.open(r'Images/number_example.PNG')
    blurred_example_number = example_number.filter(ImageFilter.GaussianBlur(radius=slider))
    st.image(blurred_example_number, width=150)

#button got pressed
if start_button:
    Unicorn_Recorder.set_backend(SawTooth)
    rec = Unicorn_recorder()
    rec.connect()
    rec.start_recording()
    inputData = []

    def get_output(countt):
        # clear all data collected before the last refresh
        while True:
            countt +=1
            rec.clear()
            time.sleep(3.7)
            rec.refresh()
            tempGetData = rec.get_new_data()
            # get the data gathered in the last second
            input = np.asarray(tempGetData)[:8]
            with open(r'C:\Users\BCI-Seminar\Documents\visual_stress_do_not_open\bison_not_seminar\EEGstream_3sec_' + str(countt), 'wb') as myfile:
                pickle.dump(tempGetData, myfile)

            # prepare and filter the data
            custom_raw = mne.io.RawArray(input, info)
            custom_raw.info['events'] = np.array([[125, 0, 1]])
            custom_raw.pick('eeg', exclude=['Fz'])
            custom_raw.filter(2, 40)
            custom_raw.set_eeg_reference("average", projection=False)
            custom_raw.apply_function(lambda a: a * 1e-7)

            epoch = mne.Epochs(
                custom_raw,
                custom_raw.info['events'],
                event_id={'foo': 1},
                tmin = 0,
                tmax = 3,
                baseline=(None, None),
                preload= True
            )
            # show the output of the model
            output = loaded_model.predict(np.asarray([epoch.get_data()[0].flatten()]))
            #predictedImageCondition = output[0]
            #agree = st.checkbox('Check to Blurr')
            #feedbackLocation.write(output)
            print(countt, 'Prediction: ', np.asarray(epoch.get_data()[0][:].flatten()), output, ' \nimageCondition:  ', imageCondition)
            #print(np.asarray(epoch.get_data()[0][:].flatten()))
    #hide options
    agree = False
    slider_position.empty()

    #use css to center the image
    with open(r"cssTemplate.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    #start the recording
    #Unicorn_Recorder.set_backend(SawTooth)
    #rec = Unicorn_recorder()
   # rec.connect()
    #rec.start_recording()

    #load the trained model
    loaded_model = pickle.load(open('model_svm_petri_3sec.pkl', 'rb'))
    info = mne.create_info(
        ch_names=['Fz', 'C3', 'Cz', 'C4', 'Pz', 'PO7', 'Oz', 'PO8'],
        ch_types='eeg',
        sfreq=250)

    # counter counts the amount of times the image changed
    counter = 0
    thread = threading.Thread(target=get_output, args=(0,))
    thread.start()
    while True:
        #counter += 1

        #load an image form the Image folder
        randomImage = random.choice(images)
        originalImage = Image.open(
            r'Images\\' + str(
                randomImage) + '.PNG')

        #load the same image but blurred
        blurredImage = originalImage.filter(ImageFilter.GaussianBlur(radius=slider))

        #show the clean image
        imageCondition = 'Not Blurred'
        imageLocation.image(originalImage, width=700)

        time.sleep(20)
        #if (predictedImageCondition == 0):
        #    feedbackLocation = st.write(predictedImageCondition)

        #show the blurry image
        imageCondition = 'Blurred'
        imageLocation.image(blurredImage, width=700)
        time.sleep(20)
        #feedbackLocation = st.write(predictedImageCondition)