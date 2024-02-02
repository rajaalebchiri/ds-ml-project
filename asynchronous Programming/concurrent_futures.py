import time
import concurrent.futures


def do_something(seconds):
    print(f"sleeping {seconds} second(s)")
    time.sleep(seconds)
    print("done sleeping")


processes = []


if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something, 1) for _ in range(10)]
        for f in concurrent.futures.as_completed(results):
            print(f.result())
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=[1.5])
    #     p.start()
    #     processes.append(p)

    # for process in processes:
    #     process.join()

    finish = time.perf_counter()

    print(f"finished in {round(finish - start, 2)} s")
