# The backend needs to be set BEFORE importing the Unicorn_recorder module
from src import Unicorn_Recorder
from src.Unicorn_Recorder.Dummies import SawTooth

Unicorn_Recorder.set_backend(SawTooth)

if __name__ == "__main__":
    # Copies the example use_a_plot
    from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
    from src.Plotter.LivePlots.SwitchPlot import SwitchPlot as Plotclass

    rec = Unicorn_recorder()
    rec.connect()
    rec.start_recording(test_signal_mode=True)
    info_queue, event_queue = rec.open_plot(1, Plotclass)
    while True:
        print(f"Recieved Event: {event_queue.get()}")
