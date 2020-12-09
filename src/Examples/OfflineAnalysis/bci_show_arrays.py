if __name__ == "__main__":
    from src.Plotter.OfflinePlots.MPLPrinter import MPLPrinter
    from src.Plotter.OfflinePlots.MPLPrinter import DetectionMode
    from src.Unicorn_Recorder.Dummies import RealData
    import mne
    import os
    from src.Utils import Utils
    PATH = r"C:\\Users\\BCI-Seminar\\Desktop\\"

    printer = MPLPrinter(250)

    files = os.listdir(PATH)
    while True:
        print("Type a command: <plot>, <show>, <exit>")
        command = input()
        if command == "plot":
            selection = int(Utils.file_slection(PATH))
            raw = mne.io.read_raw_fif(PATH + files[selection], preload=True)
            print("Raw shape ", raw)
            events = raw.info["events"]
            events = [event["list"] for event in events]
            print("Events", events)
            data = raw.get_data(RealData.UNICORN_ELECTRODES)
            print(data.shape)
        elif command == "exit":
            break
