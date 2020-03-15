from py_mp.processes.process import Process


class ProcessManager:
    """
    The purpose of the ProcessManager is to well manage processes! One of the issues commonly faced with doing Processes
    is the dangling process or zombie process. Likewise you might have processes that are somehow silently killed, and
    then there is the logging; Processes that all print to the same stdout clutter and even occasionally mangle each
    other's outputs
    """
    def __init__(self):
        # self.processes = dict()
        self.processes = list()

    def new_process(self):
        p = Process()
        self.processes.append(p)







