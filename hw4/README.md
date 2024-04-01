# Multiprocessing

Solving tasks about threading and multiprocessing

## Contents
- [Task 1](#task-1)
- [Task 2](#task-2)
- [Task 3](#task-3)

### Task 1
**Task:** 

- Take the function of counting Fibonacci numbers and compare the code execution time (calling the function from a large number `n` (so that the difference in starts on threads and processes could be seen) 10 times through 10 threads/processes) when using `threading` and `multiprocessing`
- It is necessary to compare the execution time at synchronous launching, using threads and processes. 
- Artifact - text file with the results of launching by different methods.

**Solution:**
Solution of this task is the file ```artifacts/Results_fibonacci.txt```

### Task 2
**Task:**

- Rewrite the ```integrate``` function so that its execution can be parallelized. Use `concurrent.futures`: `ThreadPoolExecutor` and `ProcessPoolExecutor`.
- Add logging (when which task is started), compare execution time for `integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs)` at different number of `n_jobs` (from 1 to cpu_num*2) when using `ThreadPoolExecutor` and `ProcessPoolExecutor`. 
- Artifact - log file, file comparing execution time in both cases depending on the number of vorkers

function ```integrate```:
```
import math
def integrate(f, a, b, *, n_jobs=1, n_iter=1000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc
```
 
**Solution:**
Solution of this task are files ```artifacts/integration.log``` and ```Results_integration.txt```

### Task 3
**Task:** 

Practice working with processes. Using `multiprocessing.Queue` and `multiprocessing.Pipe`. Implement the following application schema:
- You have a main process and 2 child processes (`A` and `B`).
- From the main process you can, via `stdin`, send messages (strings) to process `A`, which will be stored in a queue.
- To each of the messages, process `A` will apply `.lower()` and send to process `B` (one message every 5 seconds).
- Process `B` should send the encoded string through `rot13` and send it to the main process from where it should print to `stdout`.
- Artifact - text file of interaction between you and the program (message time should be output)

 
**Solution:**
Solution of this task is file ```artifacts/Result_programms_a_and_b.txt```
