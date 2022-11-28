import sys
import time
import floyd_imperative
import floyd_recursive
import test_case


def performance_check():

    NO_PATH=999
    input = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0],
    ]

    started_at = time.perf_counter()
    for _ in range(2**12):
        floyd_recursive.floyd(input)
    process_rec = time.time() - started_at

    started_at = time.perf_counter()
    for _ in range(2**12):
        floyd_imperative.floyd(input)
    process_imp = time.time() - started_at

    return (process_rec, process_imp)


if __name__ == '__main__':
    process_rec, process_imp = performance_check()
    print('recursive: {}s'.format(round(process_rec, 2)))
    print('imperative: {}s'.format(round(process_imp, 2)))

