from src import Unicorn_Recorder
from src.Unicorn_Recorder.Dummies import SawTooth
import time

Unicorn_Recorder.set_backend(SawTooth)

if __name__ == "__main__":
    # Copies the example use_a_plot
    from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
    from src.Plotter.LivePlots.SwitchPlot import SwitchPlot as Plotclass

    shortcuts = {
        "Ctrl+W": 3,  # Start
        "Ctrl+A": 2,  # Tausch
        "Ctrl+S": 1,  # Ende
        "Ctrl+D": 0
    }

    rec = Unicorn_recorder()
    rec.connect()
    rec.start_recording(test_signal_mode=True)
    info_queue, event_queue = rec.open_plot(1, Plotclass, shortcut_to_event=shortcuts)
    while True:
        print(rec.get_events())
        # The plot is slow to open just wait a bit

