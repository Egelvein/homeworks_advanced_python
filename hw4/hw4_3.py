import codecs
import multiprocessing as mp
import time
import queue


class MainProcess():
    def __init__(self, filename_stdout):
        self.queue_to_a = mp.Queue()
        self.queue_to_b = mp.Queue()
        self.filename_stdout = filename_stdout

    def send_data(self, line, lock):
        msg = line.strip()
        self.queue_to_a.put(msg)
        with lock:
            with open(self.filename_stdout, 'a') as f_stdout:
                f_stdout.write(f'Time: {time.time() % 1000:.7f}\tSent to Process A: {msg}\n')

    def receive_data(self, lock):
        while True:
            try:
                res = self.queue_to_b.get()
                with lock:
                    with open(self.filename_stdout, 'a') as f_stdout:
                        f_stdout.write(f'Time: {time.time() % 1000:.7f}\tReceived from Process B: {res[0]}\n')
            except queue.Empty:
                pass


class ProcessA():
    def __init__(self, main_process: MainProcess, pipe_entry):
        self.main = main_process
        self.pipe = pipe_entry

    def send_msg(self, msg: str):
        self.pipe.send(msg.lower())
        time.sleep(5)

    def receive_msg(self):
        while True:
            try:
                msg = self.main.queue_to_a.get()
                self.send_msg(msg)
            except queue.Empty:
                pass


class ProcessB():
    def __init__(self, main_process: MainProcess, pipe_out):
        self.main = main_process
        self.pipe = pipe_out

    def send_msg(self, msg: str):
        self.main.queue_to_b.put([msg])

    def receive_msg(self):
        while True:
            msg = self.pipe.recv()
            if msg:
                self.send_msg(codecs.encode(msg, 'rot_13'))


if __name__ == '__main__':
    filename_stdout = './artifacts/Result_programms_a_and_b_1.txt'

    a, b = mp.Pipe(duplex=False)
    lock = mp.Lock()

    main = MainProcess(filename_stdout)
    A = ProcessA(main, b)
    B = ProcessB(main, a)

    x1 = mp.Process(target=main.receive_data, args=(lock,))
    x2 = mp.Process(target=B.receive_msg, args=())
    x3 = mp.Process(target=A.receive_msg, args=())

    for x in x1, x2, x3:
        x.start()

    while True:
        main.send_data(input(), lock)
