if __name__ == "__main__":
    from src.Plotter.OfflinePlots.MPLPrinter import MPLPrinter, DetectionMode
    from src.Unicorn_Recorder.Dummies import RealData
    import mne
    import os
    from src.Utils import Utils
    PATH = r"./../SampleRecordings/"

    printer = MPLPrinter(250)

    files = os.listdir(PATH)
    while True:
        print("Type a command: <plot>, <show>, <exit>")
        command = input()
        if command == "plot":
            selection = int(Utils.file_slection(PATH))
            raw = mne.io.read_raw_fif(PATH + files[selection], preload=True)
            events = raw.info["events"]
            events = [event["list"] for event in events]
            data = raw.get_data([RealData.UNICORN_ELECTRODES[6]])
            printer.plot(data, cutoff=(250,-1), bandpass=(2,40), mode=DetectionMode.PSD)
        elif command == "show":
            printer.show()
        elif command == "exit":
            break
