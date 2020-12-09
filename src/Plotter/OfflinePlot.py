import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib import pyplot
from src.Unicorn_Recorder.Filtering import Filtering
import mne
from abc import abstractmethod


class OfflinePlot:
    """
    A class to output EEG data in a graph using interactive matplotlib
    """

    def __init__(self, sfreq: int):
        #The sampling frequency
        self.sfreq = sfreq

        self.fig, self.axe = pyplot.subplots(1,1)

    @abstractmethod
    def plot(self, data, *args):
        pass

    def data_preprocessing(self, data, car: bool, zero_mean: bool, bandpass, movAvgFilter):
        """
        Data preprocessing for any EEG data of form (channels, samples)
        :param data: the eeg data
        :param car: Wether to use common average referencing
        :param zero_mean: Whether to compute a zero mean
        :param bandpass:
        :param movAvgFilter:
        :return:
        """
        if car:
            data = Filtering.car(data)

        if zero_mean:
            data = Filtering.zero_mean(data)

        if bandpass is not None:
            data = mne.filter.filter_data(data, sfreq=self.sfreq, l_freq=bandpass[0], h_freq=bandpass[1])

        if movAvgFilter > 0:
            data = Filtering.movAvg(data, filter_size=20)

        return data

    def show(self):
        pyplot.show(self.axe)
        self.axe.clear()
        self.fig, self.axe = pyplot.subplots(1, 1)
