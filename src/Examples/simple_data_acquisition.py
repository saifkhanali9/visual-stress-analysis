from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
import time

if __name__ == "__main__":
    rec = Unicorn_recorder()
    rec.connect()
    rec.start_recording()
    while True:
        time.sleep(1)
        rec.refresh()
        print(type(rec.get_new_data()))