if __name__ == "__main__":
    from src.Plotter.OfflinePlots.MPLPrinter import MPLPrinter
    from src.Plotter.OfflinePlots.MPLPrinter import DetectionMode
    from src.Unicorn_Recorder.Dummies import RealData
    import mne
    import os
    from src.Utils import Utils
    from pathlib import Path
    datadir = Path(r'C:\Users\BCI-Seminar\PycharmProjects\bison_not_seminar\visual_stress_data')
    inputdatapath = datadir / '20-4_blur4px_font20pt_sansserif_count9_no1.fif'
    printer = MPLPrinter(250)

    raw = mne.io.read_raw_fif(inputdatapath, preload=True)
    print("Raw shape ", raw)
    events = raw.info["events"]
    events = [event["list"] for event in events]
    print("Events", events)
    data = raw.get_data(RealData.UNICORN_ELECTRODES)
    print(data.shape)
    for e in events:
        print(e)

    channeldata = data[:8, :]
    print(channeldata.shape)

    X = []
