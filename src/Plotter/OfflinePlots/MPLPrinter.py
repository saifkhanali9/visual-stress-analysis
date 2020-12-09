import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib import pyplot
from src.Unicorn_Recorder.Filtering import Filtering
import  mne
from scipy import signal
from scipy.fftpack import fft
import numpy
from enum import Enum

from src.Plotter.OfflinePlot import OfflinePlot


class DetectionMode(Enum):
    """
    An auxillary class for MPLPrinter.
    Sets which domain values should be displayed in.
    """
    TIME = 0
    PSD = 1
    FFT = 2
    FFT_ABS = 3
    FFT_RI = 4


class MPLPrinter(OfflinePlot):
    """
    A class to output EEG data in a graph using interactive matplotlib
    """

    def __init__(self, sfreq: int):
        OfflinePlot.__init__(self, sfreq)

    def plot(self, data, zero_mean=False, car=False, bandpass=None, cutoff=(0, -1), mode=DetectionMode.TIME,
             label_detail=100, channels=None, label_freq_detail=2, title="", movAvgFilter: int=0, events: list=None,
             vertical_offset=0):
        """
        Plots EEG data to a graph
        :param data: The EEG data given as a numpy matrix of shape(channels, samples)
        :param zero_mean: Whether to subtract the mean from the time signal. (Useless when bandpass filtering)
        :param car: Whether to apply common average referencing
        :param bandpass: when set to none no filter is applied. When seet to (x,y) sets a bandpass filter between xHz and YHz
        :param cutoff: To cutoff data in the beginning of the signal
        :param mode: The domain to display the data in
        :return: None
        """

        channels = list(range(data.shape[0])) if channels is None else channels
        events = [] if events is None else events

        data = data[:, cutoff[0]:cutoff[1] if cutoff[1] > -1 else data.shape[1]]
        data = self.data_preprocessing(data, car, zero_mean, bandpass, movAvgFilter)

        if mode == DetectionMode.TIME:
            for i in range(len(channels)):
                self.axe.plot(data[channels[i], :] + vertical_offset*i, label=f"Channel: {channels[i]}")
            for event in events:
                pyplot.axvline(event[2], label=f"Event: {event[0] >> 4:0{4}b} {event[0] % 0b10000:0{4}b}", c="r")
                self.axe.annotate(f"Event: {event[0] >> 4:0{4}b} {event[0] % 0b10000:0{4}b}", xy=(event[2], 10))
            self.axe.legend()
        elif mode == DetectionMode.PSD:
            for channel in channels:
                psd = signal.periodogram(data[channel, :], self.sfreq)
                labels = []
                positions = []
                for j in range(len(psd[0])):
                    if j % label_detail == 0:
                        positions.append(j)
                        labels.append(f"{psd[0][j]:.{label_freq_detail}f}")

                self.axe.set_xticks(positions)
                self.axe.set_xticklabels(labels)
                self.axe.plot(psd[1], label=f"Channel: {channel}")
        elif mode == DetectionMode.FFT or mode == DetectionMode.FFT_ABS or mode == DetectionMode.FFT_RI:
            for channel in channels:
                fft_results = fft(data[channel, :])

                positions = numpy.array(range(1,len(fft_results)+1, label_detail))
                label_freqs = positions / len(fft_results) * self.sfreq
                labels = [f"{pos:.{label_freq_detail}f}" for pos in label_freqs]

                self.axe.set_xticks(positions)
                self.axe.set_xticklabels(labels)

                if not mode == DetectionMode.FFT_ABS:
                    self.axe.plot(numpy.real(fft_results), label=f"Real Channel: {channel}")
                    self.axe.plot(numpy.imag(fft_results), label=f"Imaginary Channel: {channel}")
                if not mode == DetectionMode.FFT_RI:
                    self.axe.plot(numpy.absolute(fft_results), label=f"Absolute Channel: {channel}")

