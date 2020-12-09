from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder

# Try activating different plot classes here to see the functionality
from src.Plotter.LivePlots.SwitchPlot import SwitchPlot as Plotclass
#from Plotter.Plots.SwitchPlot import SwitchPlot as Plotclass

# Note that since we are working with multiple processes this if clause is necessary.
if __name__ == "__main__":
    rec = Unicorn_recorder()
    rec.connect()
    rec.start_recording(test_signal_mode=False)
    rec.open_plot(1, Plotclass)
    while True:
        # Do what ever you like with the data in the mean time
        pass
