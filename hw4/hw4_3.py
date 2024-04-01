import multiprocessing
import time
import queue
import codecs
from datetime import datetime

def process_a(queue_ab, queue_ba):
    while True:
        try:
            message, timestamp = queue_ab.get(timeout=1)
            message_lower = message.lower()
            queue_ba.put((message_lower, timestamp))
        
        except queue.Empty:
            pass

def process_b(queue_ba):
    while True:
        try:
            message_lower, timestamp = queue_ba.get(timeout=1)
            message_rot13 = codecs.encode(message_lower, 'rot_13')
            queue_ba.put((message_rot13, timestamp))
        
        except queue.Empty:
            pass


if __name__ == '__main__':
    queue_ab = multiprocessing.Queue()
    queue_ba = multiprocessing.Queue()

    process_a = multiprocessing.Process(target=process_a, args=(queue_ab, queue_ba))
    process_b = multiprocessing.Process(target=process_b, args=(queue_ba,))

    process_a.start()
    process_b.start()

    with open('artifacts/Result_programms_a_and_b.txt', 'w') as f:
        try:
            while True:
                message = input("Enter message: ")
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sent to Process A: {message}\n")
                queue_ab.put((message, datetime.now()))
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sent to Process A: {message}")

                encoded_message, timestamp = queue_ba.get()
                f.write(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] Received from Process B: {encoded_message}\n")
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Received from Process B: {encoded_message}")

                time.sleep(5)

        except KeyboardInterrupt: # Ctrl + C
            process_b.terminate()

