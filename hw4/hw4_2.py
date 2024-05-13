from concurrent.futures import as_completed, Executor, ProcessPoolExecutor, ThreadPoolExecutor, wait
import math
import time

def report(data_center: str, workers: int, timing: float):
    with open('./artifacts/Results_integration_1.txt', 'a') as f:
        f.write(f'{data_center}, jobs: {workers}, time: {timing:.3f}\n')

def segment_integral(func, initial, step, start, stop):
    result = 0
    for i in range(start, stop):
        result += func(initial + i * step) * step
    return result

def integrate(func, initial, end, data_center: str, workers: int = 1, iterations: int = 50000000):
    if data_center == 'ProcessPoolExecutor':
        center = ProcessPoolExecutor(workers)
    elif data_center == 'ThreadPoolExecutor':
        center = ThreadPoolExecutor(workers)
    else:
        return 0

    total_area = 0
    step = (end - initial)/iterations

    with open('./artifacts/integration_1.txt', 'a') as log_file:
        log_file.write(f'{data_center}, {workers} jobs, {time.time() % 10000}\n')

    start_time = time.time()
    tasks = []
    for i in range(workers):
        section = math.ceil(iterations / workers)
        start_index = i * section
        end_index = min(iterations, start_index + section)
        tasks.append(center.submit(segment_integral, func, initial, step, start_index, end_index))

    total_area = sum([task.result() for task in tasks])
    end_time = time.time()
    report(data_center, workers, end_time - start_time)

    with open('./artifacts/integration_1.txt', 'a') as log_file:
        log_file.write(f'{data_center} with {workers} workforce completed! Result: {total_area:.3f}, time: {end_time - start_time}\n\n')

    return total_area

if __name__ == '__main__':
    for workers in range(1, 17):
        integrate(math.cos, 0, math.pi/2, 'ThreadPoolExecutor', workers)
    with open('./artifacts/Results_integration_1.txt', 'a') as f:
        f.write('\n')
    for workers in range(1, 17):
        integrate(math.cos, 0, math.pi/2, 'ProcessPoolExecutor', workers)
