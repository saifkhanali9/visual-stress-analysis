import mne
import streamlit as st
#import streamlit.components.v1 as components
import sys
sys.path.insert(0, r'C:\Users\BCI-Seminar\Documents\visual_stress_do_not_open\bison_not_seminar')
from PIL import Image
from PIL import ImageFilter
import numpy as np
import time
import random
from src import Unicorn_Recorder
from src.Unicorn_Recorder.Dummies import SawTooth
import pickle
from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
loaded_model = pickle.load(open('dummyModel.sav', 'rb'))
info = mne.create_info(
        ch_names=['Fz', 'C3', 'Cz', 'C4', 'Pz', 'PO7', 'Oz', 'PO8'],
        ch_types='eeg',
        sfreq=250)
if __name__ == '__main__':
    rec = Unicorn_recorder()
    rec.connect()
    rec.start_recording()
    rec.clear()
    time.sleep(1.5)
    rec.refresh()
    input = np.array(rec.get_new_data())[:8, :250]
    custom_raw = mne.io.RawArray(input, info)
    custom_raw.filter(2, 40)
    custom_raw.set_eeg_reference("average", projection=False)
    print(custom_raw.get_data())
    print(len(input))
    print(loaded_model.predict([custom_raw.get_data().flatten()]))