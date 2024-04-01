import threading
import multiprocessing
import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def run_sync(n):
    start_time = time.time()
    
    for _ in range(10):
        fibonacci(n)
    
    end_time = time.time()
    
    return end_time - start_time

def run_threads(n):
    start_time = time.time()
    threads = []
    
    for _ in range(10):
        thread = threading.Thread(target=fibonacci, args=(n,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    
    return end_time - start_time

def run_processes(n):
    start_time = time.time()
    processes = []

    for _ in range(10):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        process.start()
        processes.append(process)
    
    for process in processes:
        process.join()
    
    end_time = time.time()
    
    return end_time - start_time

n = 35

time_sync = run_sync(n)
print('Sync is ready')
time_threads = run_threads(n)
print('Threads is ready')
time_processes = run_processes(n)
print('Processes is ready')

with open('artifacts/Results_fibonacci.txt', 'w') as file:
    file.write('Method\t\t\tTime\n')
    file.write(f'Sync\t\t\t{time_sync}\n')
    file.write(f'Threads\t\t\t{time_threads}\n')
    file.write(f'Processes\t\t{time_processes}\n')


