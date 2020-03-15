import time

from py_mp.processes.pipe_process import PipeProducerProcess, pipe_process_pair

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed

def rate(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int(1/(te - ts))
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, 1/(te - ts)))
        return result
    return timed

def repeat(argument):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for _ in range(argument):
                function(*args, **kwargs)
        return wrapper
    return decorator



def benchmark_pipe_processes():

    cons, prod = pipe_process_pair()

    def produce_fn():


    @rate
    @repeat(10 ** 6)
    def produce_consume():
        prod.produce('abc')
        cons.consume()

    produce_consume()

if __name__ == '__main__':
    benchmark_pipe_processes()