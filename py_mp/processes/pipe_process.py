import time

from py_mp.processes.process import ProducerProcess, ConsumerProcess
from multiprocessing import Pipe

DEFAULT_GRACE_PERIOD = 1


class PipeProducerProcess(ProducerProcess):

    def __init__(self, pipe, producer_fn=None, rate_limit=None):
        self.pipe = pipe
        self.__producer_fn = producer_fn
        self.rate_limit = rate_limit

    # def produce(self):

    def run(self):
        sleep_time = None
        if self.rate_limit:
            sleep_time = 1 / self.rate_limit
        while True:
            x = self.__producer_fn()
            self.pipe.send(x)
            if sleep_time:
                time.sleep(sleep_time)


class PoisonPill:
    pass


class PipeConsumerProcess(ConsumerProcess):

    def __init__(self, pipe, consume_fn=None, on_close_fn=lambda: _):
        super().__init__(consume_fn)
        self.pipe = pipe
        self.on_close_fn = on_close_fn

    def stop(self):
        # If the pipe is duplex we can try to send a poison pill
        if self.pipe.writable:
            self.pipe.send(PoisonPill)
            time.sleep(DEFAULT_GRACE_PERIOD)
        super().stop() # Let higher ups handle it

    def run(self):
        while self.stop:
            try:
                x = self.pipe.recv()  # Blocks until something to read
                if x is PoisonPill:
                    break
                self.consume_fn(x)
            except EOFError:
                break


# Create two matching pipe processes, one consumer, one producer
def pipe_process_pair():
    recv, send = Pipe()
    return PipeConsumerProcess(recv), PipeProducerProcess(send)
