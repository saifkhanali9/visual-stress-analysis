if __name__ == "__main__":
    from src.Plotter.OfflinePlots.MPLPrinter import MPLPrinter
    from src.Unicorn_Recorder.Dummies import RealData
    import mne
    import os
    from src.Utils import Utils
    PATH = r"C:\Users\BCI-Seminar\PycharmProjects\bison_not_seminar\\"

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
            data = raw.get_data(RealData.UNICORN_ELECTRODES[:8])
            print('THIS IS THE DATA', data)
            with open(r'C:\Users\BCI-Seminar\PycharmProjects\bison_not_seminar\numpy_array.txt', 'w') as f:
                for i in range(len(data)):
                    for j in data[i]:
                        f.write(str(j) + ', ')

                    f.write('\n' +str(i+1) +':\n-------------------------------------\n\n\n')
            f.close()
            printer.plot(data)
        elif command == "show":
            printer.show()
        elif command == "exit":
            break
