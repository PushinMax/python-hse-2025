import math
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

def integrate(f, a, step, start_idx, end_idx):
    acc = 0
    for j in range(start_idx, end_idx):
        acc += f(a + j * step) * step
    return acc


def integrate_thread(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        futures = []
        for job_number in range(n_jobs):
            start_idx = int(n_iter * job_number / n_jobs)
            end_idx = int(n_iter * (job_number + 1) / n_jobs)

            future = executor.submit(integrate, f, a, step, start_idx, end_idx)
            futures.append(future)

        for future in futures:
            acc += future.result()
    return acc


def integrate_process(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    res = []
    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        futures = []
        for job_number in range(n_jobs):
            start_idx = int(n_iter * job_number / n_jobs)
            end_idx = int(n_iter * (job_number + 1) / n_jobs)

            future = executor.submit(integrate, f, a, step, start_idx, end_idx)
            futures.append(future)

        for future in futures:
            res.append(future.result())
    return sum(res)

if __name__ == "__main__":
    num = multiprocessing.cpu_count()
    for i in range (1, num * 2):
        start_time = time.time()
        val = integrate_thread(math.cos, 0, math.pi / 2, n_jobs=i, n_iter=10000000)
        end_time = time.time()
        print(f"Время выполнения через треды на {i} потоках: {end_time - start_time:.4f} секунд. Результат: {val:.4f}")


    for i in range (1, num * 2):
        start_time = time.time()
        val = integrate_process(math.cos, 0, math.pi / 2, n_jobs=i, n_iter=10000000)
        end_time = time.time()
        print(f"Время выполнения через процессы на {i} потоках: {end_time - start_time:.4f} секунд. Результат: {val:.4f}")

