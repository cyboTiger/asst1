## Q3
### 2 threads
Thread 0 takes 242.561 ms
Thread 1 takes 247.833 ms
Measuring performance of 2 thread, speedup is 1.971814x

### 3 threads
Thread 0 takes 109.501 ms
Thread 2 takes 112.757 ms
Thread 1 takes 323.269 ms
Measuring performance of 3 thread, speedup is 1.645569x

### 4 threads
Thread 0 takes 48.156 ms
Thread 3 takes 53.008 ms
Thread 1 takes 207.134 ms
Thread 2 takes 208.381 ms
Measuring performance of 4 thread, speedup is 2.383136x

### 5 threads
Thread 0 takes 29.640 ms
Thread 4 takes 29.866 ms
Thread 1 takes 143.144 ms
Thread 3 takes 145.283 ms
Thread 2 takes 210.473 ms
Measuring performance of 5 thread, speedup is 2.500376x

### 6 threads
Thread 0 takes 13.540 ms
Thread 5 takes 15.627 ms
Thread 4 takes 69.027 ms
Thread 1 takes 76.332 ms
Thread 2 takes 128.666 ms
Thread 3 takes 129.814 ms
Measuring performance of 6 thread, speedup is 3.177569x

### 7 threads
Thread 0 takes 16.119 ms
Thread 6 takes 16.544 ms
Thread 1 takes 63.965 ms
Thread 5 takes 67.067 ms
Thread 4 takes 116.785 ms
Thread 2 takes 122.088 ms
Thread 3 takes 158.520 ms
Measuring performance of 7 thread, speedup is 3.343038x

### 8 threads
Thread 0 takes 8.274 ms
Thread 7 takes 12.686 ms
Thread 1 takes 39.185 ms
Thread 6 takes 38.954 ms
Thread 2 takes 77.570 ms
Thread 5 takes 77.913 ms
Thread 4 takes 111.822 ms
Thread 3 takes 113.778 ms
Measuring performance of 8 thread, speedup is 3.924903x

## Q4
The original method split the whole picture into contiguous rows and allocate these chunks to different threads. This can ensure that all but the last threads handle the same amount of computation. However, this can become problematic when the total number of rows is not divisible by numThreads, and will render the last thread handling more computation, which has a significant impact on the whole performance because the total running time is dependent on the slowest thread.

The new method let every thread start from the threadid-th row, and process the next numThread-th row until reaching the end of the picture. This can ensure that each thread will handle the same amount of computation(no more than one row in difference). So this implementation achieves perfectly evenly distributred workloads. Thus it can achieve almost linear speedup w.r.t numThreads.

## Q5
Yes. Like I said in Q4.