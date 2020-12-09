if __name__ == "__main__":
    from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
    import time

    rec = Unicorn_recorder()
    rec.connect()
    rec.start_recording()
    time.sleep(20)
    rec.set_event(1)
    rec.refresh()
    rec.stop_recording(wait=True)                  # Set this to wait until the recording was actually stopped
    rec.refresh()                                  # the save function only considers values that were refreshed
    rec.save("test.fif", overwrite=True)           # Saves to desktop per default.
    rec.disconnect()
    rec.close_remote()
