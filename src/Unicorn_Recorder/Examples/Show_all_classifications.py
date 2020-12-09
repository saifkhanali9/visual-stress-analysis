if __name__ == "__main__":
    from src.Plotter.OfflinePlots.ClassificationPlot import ClassificationPlot
    from src.Unicorn_Recorder.Dummies import RealData
    from src.Classifiers.SSVEP_Classifier.ssvep_classifer import SSVEP_Classfier as Classifier
    #from src.SSVEP_Classifier.psd_classifer import PSD_Classfier as Classifier
    #from src.Classifiers.SignalQualityClassifier import SignalQualityClassifier as Classifier
    import mne
    import os
    from src.Utils import Utils
    PATH = r"C:\Users\Tobias\Desktop\DFKI Recordings\22.05\\"
    sfreq = 250

    classifier = Classifier(sfreq, frequencies_to_detect=[10, 15], harmonics_depth=3)
    printer = ClassificationPlot(classifier, sfreq=sfreq)

    files = os.listdir(PATH)
    while True:
        print("Type a command: <plot>, <show>, <exit>")
        command = input()
        if command == "plot":
            selection = Utils.file_slection(PATH)
            raw = mne.io.read_raw_fif(PATH + files[selection], preload=True)
            data = raw.get_data(RealData.UNICORN_ELECTRODES)
            print(data.shape)
            printer.plot(data, bandpass=(2, 40), car=False, cutoff=(250, -1), label_detail=1, label_freq_detail=0,
                         channels=list(range(8)), movAvgFilter=-1, clamp=False, overlap=125, show_conf=True)
        elif command == "show":
            printer.show()
        elif command == "exit":
            break
