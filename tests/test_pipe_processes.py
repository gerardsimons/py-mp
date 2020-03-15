import unittest

from py_mp.processes.pipe_process import pipe_process_pair


class TestPipeProcesses(unittest.TestCase):

    def setUp(self) -> None:
        self.cons, self.prod = pipe_process_pair()

    def test_simple(self):
        pipe_in = b'abc'
        self.prod.produce(pipe_in)
        pipe_out = self.cons.consume()

        self.assertEqual(pipe_in, pipe_out)


