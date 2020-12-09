from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
from src import Unicorn_Recorder
import UnicornPy
Unicorn_Recorder.set_backend(UnicornPy)
import time

if __name__ == "__main__":
    rec = Unicorn_recorder()
    rec.connect()
    rec.start_recording(test_signal_mode=True)
    while True:
        time.sleep(1)
        rec.refresh()
        print(rec.get_new_data())
