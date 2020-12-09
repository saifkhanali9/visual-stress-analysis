import pytec_recorder as pyrec

rec = pyrec.PytecRecorder(doQuickStart=False) # YOu can't use the quickstart anymore if you are using no Plot
rec.newSession()
rec.setAllParameters()
rec.connect()
rec.doImpedanceCheck()
rec.startRecording()
while True:
    print(rec.dataEEG.shape)  # The EEG data. Be careful not to change the array as the recorder will save this array.
    rec.sleepAndRecord(1)  # The EEG only updates the array if you call this function.
    someOffset = 0  # Use this to offset the timestamp in samples.
    rec.setEvent(1, offsetCaller=someOffset)  # Creates a timestamp in the data, at the last time sleepAndRecord was called.
                                              # The first value is an id the id that the event will be saved under.
rec.stopRecording()
rec.saveRecording2File()
rec.disconnect()
