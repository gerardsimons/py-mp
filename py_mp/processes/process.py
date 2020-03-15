import multiprocessing as mp
from abc import abstractmethod

# A slightly more safe Process
class Process(mp.Process):

    def __init__(self, daemon=True):
        super().__init__()
        self.stop_event = mp.Event()
        self.daemon = daemon

    def stop(self):
        self.stop_event.set()


class ProducerProcess:

    def __init__(self, produce_fn):
        super().__init__()
        self.__produce_fn = produce_fn

    # def run(self):
    #     while True:
    #

class ConsumerProcess(Process):

    def __init__(self, consume_fn):
        super().__init__()
        self.__consume_fn = consume_fn

    @abstractmethod
    def consume(self):
        pass


