import asyncio
import websockets
import time


async def hello(websocket, path):
    await websocket.send("hello")
    print(f"> connected")

    from src import Unicorn_Recorder
    from src.Unicorn_Recorder.Dummies import SawTooth
    from src.Plotter.LivePlots.SwitchPlot import SwitchPlot as Plotclass
    Unicorn_Recorder.set_backend(SawTooth)

    from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder

    rec = Unicorn_recorder()
    rec.connect()
    rec.start_recording()
    await asyncio.sleep(1)

    time_exp = 20
    epochs = 4
    await websocket.send('hide')
    await asyncio.sleep(10)

    for _ in range(epochs):
        """
        Focus state : focused (label is 0)

        """
        print('focus')
        rec.refresh()
        rec.set_event(0)
        await websocket.send('focus')
        await asyncio.sleep(time_exp)
        """
        Focus state : unfocused (label is 1)

        """
        print('blur')
        rec.refresh()
        rec.set_event(1)
        await websocket.send('blur')
        await asyncio.sleep(time_exp)

    await websocket.send('hide')

    rec.refresh()
    rec.stop_recording(wait=True)                  # Set this to wait until the recording was actually stopped
    rec.refresh()                                  # the save function only considers values that were refreshed
    rec.save("gel_petri_20-4_blur3.3px_font24pt_sansserif_count8_no4.fif", path=r"C:\Users\BCI-Seminar\Documents\visual_stress_do_not_open\bison_not_seminar\visual_stress_data\\", overwrite=True)           # Saves to desktop per default.
    #rec.save("test.fif", overwrite=True)           # Saves to desktop per default.

    rec.disconnect()
    rec.close_remote()


if __name__ == "__main__":
    ws = websockets.serve(hello, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(ws)
    asyncio.get_event_loop().run_forever()
