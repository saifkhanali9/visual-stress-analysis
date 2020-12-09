from src.Plotter.LivePlots.SwitchPlot import SwitchPlot as Plotclass
from src import Unicorn_Recorder
from src.Unicorn_Recorder.Dummies import RealData

Unicorn_Recorder.set_backend(RealData)
#"C:\\Users\\BCI-Seminar\\Desktop\\20-4_blur4px_font20pt_sansserif_count9_no1.fif"
#C:\\Users\\BCI-Seminar\\Documents\\visual_stress_do_not_open\\bison_not_seminar\\visual_stress_datapetri_20-4_blur3.3px_font24pt_sansserif_count8_no2.fif
RealData.set_file_path("C:\\Users\\BCI-Seminar\\Documents\\visual_stress_do_not_open\\bison_not_seminar\\visual_stress_data\\visual_stress_datapetri_20-4_blur3.3px_font24pt_sansserif_count8_no10.fif")  # Set your own file path here
RealData.set_electrodes(RealData.UNICORN_ELECTRODES)

if __name__ == "__main__":
    from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder

    rec = Unicorn_recorder()
    rec.connect()
    rec.start_recording()
    rec.open_plot(1, Plotclass)
