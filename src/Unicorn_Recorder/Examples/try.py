from src.Utils import Utils
import expyriment
from expyriment import control, design, io, misc, stimuli
import expyriment.misc.geometry

n_blocks=1
n_trials_block=4
TONE_DURATION=500
stim=['>>>>>>>>>>','<<<<<<<<<<']

if __name__ == "__main__":
    from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
    import time
    #Unicorn_recorder.check_signal_quality(data, Unicorn_recorder.get_sfreq()) --> Quality per channel

    #PATH = "C:/Users/BCI-Seminar/Desktop/BCI_Seminar_Microscope/recorded_data_MI/"
    exp = expyriment.design.Experiment(name="Motor_Imagery")
    expyriment.control.initialize(exp)
    fixcross = expyriment.stimuli.FixCross((400, 400), position=(0, 0), line_width=20)
    fixcross.preload()

    movetext=expyriment.stimuli.TextLine(text="move hand", text_size=80)
    movetext.preload()

    tone = expyriment.stimuli.Tone(TONE_DURATION, 500)
    tone.preload()

    rec = Unicorn_recorder()
    rec.connect()
    rec.start_recording()
    #time.sleep(7)

    for block in range(n_blocks):
        temp_block = expyriment.design.Block(name=str(block + 1))
        for trial in range(n_trials_block):
            curr_stim = stim[0]
            temp_stim = expyriment.stimuli.TextLine(text=curr_stim, text_size=80)
            temp_trial = expyriment.design.Trial()
            temp_trial.add_stimulus(temp_stim)
            temp_block.add_trial(temp_trial)
        # temp_block.shuffle_trials() #is this necessary
        exp.add_block(temp_block)

    # fixcross.plot(tone)

    expyriment.control.start(skip_ready_screen=True)

    for block in exp.blocks:
        for trial in block.trials:
            fixcross.present()
            tone.present()
            exp.clock.wait(1000)
            fixcross.present()
            exp.clock.wait(500)
            trial.stimuli[0].present()
            exp.clock.wait(2500)
            movetext.present()
            exp.clock.wait(500)
            exp.clock.reset_stopwatch()
            #exp.clock.wait(1000)

    expyriment.control.end()

    rec.set_event(1)

    rec.refresh()
    rec.stop_recording(wait=True)                  # Set this to wait until the recording was actually stopped
    rec.refresh()                                  # the save function only considers values that were refreshed
    rec.save("Akib_060820_right_1.fif", overwrite=True)           # Saves to desktop per default.
    rec.disconnect()
    rec.close_remote()









