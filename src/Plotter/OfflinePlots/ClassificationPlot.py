import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib import pyplot
from src.Unicorn_Recorder.Filtering import Filtering
import mne
from src.Classifiers.SSVEP_Classifier.classifier import Classifier
from src.Plotter.OfflinePlot import OfflinePlot
import numpy


class ClassificationPlot(OfflinePlot):
    """A plot across time for classification correlations"""

    def __init__(self, classifier: Classifier, sfreq: int=250):
        OfflinePlot.__init__(self, sfreq)
        self.classifier = classifier

    def plot(self, data, zero_mean=False, car=False, bandpass=None, cutoff=(0, -1), label_detail=100,
             label_freq_detail=2, channels=None, title="", movAvgFilter=0, clamp=True, overlap=0, baselines=None, events=None, show_conf=True):
        self.axe.set_title(title)
        channels = [] if channels is None else channels

        data = data[:, cutoff[0]:cutoff[1] if cutoff[1] > -1 else data.shape[1]]

        if car:
            data = Filtering.car(data)

        if zero_mean:
            data = Filtering.zero_mean(data)

        if bandpass is not None:
            data = mne.filter.filter_data(data, sfreq=self.sfreq, l_freq=bandpass[0], h_freq=bandpass[1])

        if movAvgFilter > 0:
            data = Filtering.movAvg(data, filter_size=20)

        classifications = numpy.zeros((2,1))
        print(classifications.shape)
        #for _ in self.classifier.frequencies_to_detect:
        #    numpy.append([])
        for x in range(int(data.shape[1] / (self.classifier.data_size - overlap))):
            to_classify = data[:, (self.classifier.data_size - overlap)*x:
                                  (self.classifier.data_size-overlap)*x+self.classifier.data_size]
            if data.shape[1] < self.classifier.data_size:
                continue
            classification = numpy.array([confidence for freq, confidence in self.classifier.classify(to_classify)])
            classification = classification.reshape((2,1))
            classifications = numpy.append(classifications, classification, axis=1)
        classifications = classifications[:, 1:]

        positions = []
        labels = []
        for j in range(int(data.shape[1]/(self.classifier.data_size-overlap))):

            positions.append(j)
            labels.append(f"{j*(self.classifier.data_size-overlap)/self.sfreq:.{label_freq_detail}f}")
        self.axe.set_xticks(positions)
        self.axe.set_xticklabels(labels)

        if show_conf:
            for classification in classifications:
                classification = classification - numpy.average(classifications, axis=0)
                self.axe.plot(classification)
            self.axe.legend([str(freq) for freq in self.classifier.frequencies_to_detect])
        else:
            self.axe.plot(numpy.argmin(classifications, axis=0), "bo")
            self.axe.legend([f"{self.classifier.frequencies_to_detect}"])




        if clamp:
            pyplot.ylim((0, 1))

    def show(self):
        pyplot.show(self.axe)
        self.axe.clear()
        self.fig, self.axe = pyplot.subplots(1, 1)
