import multiprocessing
import math
import time

def cpu_stress():
    while True:
        # Some pointless calculations to stress CPU
        math.factorial(500000)

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"Starting stress test on {num_cores} cores...")

    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
        processes.append(p)

    try:
        # Keep main process alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping stress test...")
        for p in processes:
            p.terminate()
        for p in processes:
            p.join()
