import math
import concurrent.futures
import logging
import multiprocessing
import time

def integrate(f, a, b, *, n_jobs=1, n_iter=1000):
    acc = 0
    step = (b - a) / n_iter

    def compute_chunk(start, end):
        chunk_acc = 0
        
        for i in range(start, end):
            chunk_acc += f(a + i * step) * step
        
        return chunk_acc

    if n_jobs == 1:
        acc = compute_chunk(0, n_iter)
    
    else:
        chunk_size = n_iter // n_jobs
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
            futures = []
            
            for i in range(n_jobs):
                start = i * chunk_size
                end = (i + 1) * chunk_size if i < n_jobs - 1 else n_iter
                futures.append(executor.submit(compute_chunk, start, end))
            
            for future in concurrent.futures.as_completed(futures):
                acc += future.result()

    return acc

def comparing():
    logging.basicConfig(filename='artifacts/integration.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    cpu_num = multiprocessing.cpu_count()

    n_jobs_values = list(range(1, cpu_num * 2 + 1))

    results_threadpool = {}
    results_processpool = {}

    for n_jobs in n_jobs_values:
        logging.info(f'Starting ThreadPoolExecutor with {n_jobs} workers')
        start_time_threadpool = time.time()
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        end_time_threadpool = time.time()
        elapsed_time_threadpool = end_time_threadpool - start_time_threadpool
        results_threadpool[n_jobs] = elapsed_time_threadpool
        logging.info(f'ThreadPoolExecutor with {n_jobs} workers finished in {elapsed_time_threadpool:.4f} seconds')

        logging.info(f'Starting ProcessPoolExecutor with {n_jobs} workers')
        start_time_processpool = time.time()
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        end_time_processpool = time.time()
        elapsed_time_processpool = end_time_processpool - start_time_processpool
        results_processpool[n_jobs] = elapsed_time_processpool
        logging.info(f'ProcessPoolExecutor with {n_jobs} workers finished in {elapsed_time_processpool:.4f} seconds')

    with open('artifacts/Results_integration.txt', 'w') as file:
        file.write('n_jobs\tThreadPoolExecutor\tProcessPoolExecutor\n')
        
        for n_jobs in n_jobs_values:
            file.write(f'{n_jobs}\t{results_threadpool[n_jobs]}\t{results_processpool[n_jobs]}\n')

if __name__ == "__main__":
    comparing()
