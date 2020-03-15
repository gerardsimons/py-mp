from py_mp.processes.process import ProducerProcess, ConsumerProcess


class QueueProducerProcess(ProducerProcess):
    """
    The Queue producer like other producer has a producer function that returns a piece of serializable data that is
    then put on a queue. It is expected that this function blocks if nothing is to do, or the queue size is set at such
    a size that it will block automatically when there is enough of a backlog and we should wait for the consumer to process them first.
    Another option is defining a rate at which the rate limit
    """

    def __init__(self, queue, producer_fn):
        super().__init__(producer_fn)
        self.queue = queue
        pass

    def

    def run(self):
        while True:
            x = self.__produce_fn()
            self.queue.put(x)

class QueueConsumerProcess(ConsumerProcess):

    def __init__(self):
        super().__init__()
        pass

