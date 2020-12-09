# The backend needs to be set BEFORE importing the Unicorn_recorder module
from src import Unicorn_Recorder
from src.Unicorn_Recorder.Dummies import RealData
from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
from src.Plotter.LivePlots.SwitchPlot import SwitchPlot as Plotclass
import multiprocessing
Unicorn_Recorder.set_backend(RealData)
RealData.set_file_path(r"")  # Set your own file path here
RealData.set_electrodes(RealData.UNICORN_ELECTRODES)

if __name__ == "__main__":
    event_queue = multiprocessing.Queue()
    rec = Unicorn_recorder()
    rec.connect()
    rec.start_recording()
    rec.toggle_plot(1, Plotclass, event_queue=event_queue)
    while True:
        pass
