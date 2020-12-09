import unittest
import numpy


class UnicornRecorderTests(unittest.TestCase):

    def test_check_signal_quality(self):
        from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
        matrix = numpy.array([list(range(250)),list(range(250))])
        Unicorn_recorder.check_signal_quality(matrix, 250)

    def test_check_signal_quality_1_below(self):
        from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
        matrix = numpy.array([list(range(59)),list(range(59))])
        Unicorn_recorder.check_signal_quality(matrix, 250)

    def test_check_signal_quality_1(self):
        from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
        matrix = numpy.matrix([list(range(1)),list(range(1))])
        Unicorn_recorder.check_signal_quality(matrix, 250)

    def test_stdv(self):
        from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
        matrix = numpy.array([list(range(250)),list(range(250))])
        Unicorn_recorder.check_std(matrix)

    def test_bpmd(self):
        from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
        matrix = numpy.array([list(range(250)),list(range(250))])
        Unicorn_recorder.check_bpmd(matrix, 250)

    def test_bpmd_empty(self):
        from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
        matrix = numpy.array([[0],[0]])
        Unicorn_recorder.check_bpmd(matrix, 250)

    def test_bpmd_1_below(self):
        from src.Unicorn_Recorder.unicorn_recorder import Unicorn_recorder
        matrix = numpy.matrix([list(range(59)), list(range(59))])
        Unicorn_recorder.check_bpmd(matrix, 250)
