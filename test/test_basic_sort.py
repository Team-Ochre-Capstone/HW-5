import pytest
import numpy as np
import time
import psutil
import os
import random
import gc
from basic_sort_UNIQUE_SUFFIX.int_sort import bubble, quick, insertion

# --- CONSTANTS AND SETUP ---
LIST_SIZE = 15000
NUM_ITERATIONS = 1
PERFORMANCE_TEST_LIST = [random.randint(1, 10000) for _ in range(LIST_SIZE)]
EXPECTED_SORTED = sorted(PERFORMANCE_TEST_LIST)
CURRENT_PROCESS = psutil.Process(os.getpid())


def is_sorted(int_list):
    # Testing oracle. Checks if a list of integers is sorted.

    return all(a <= b for a, b in zip(int_list, int_list[1:]))


@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    return [
        [3, 2, 1],
        [1, 1, 1],
        list(np.random.randint(low=-10, high=200, size=5)),
    ]


def test_bubble(int_lists):
    # Verifies bubble sort and measures CPU usage (Task 2a).

    # 1. FUNCTIONALITY CHECK
    for original_list in int_lists:
        assert is_sorted(bubble(original_list))

    # 2. PERFORMANCE MEASUREMENT (CPU Usage)

    # Measure CPU Usage
    CURRENT_PROCESS.cpu_percent()  # Prime the measurement
    time.sleep(0.01)

    cpu_before = CURRENT_PROCESS.cpu_percent()

    for _ in range(NUM_ITERATIONS):
        list_copy = PERFORMANCE_TEST_LIST[:]
        bubble(list_copy)

    # Measure CPU usage over the last 0.1s interval which includes the work
    cpu_after = CURRENT_PROCESS.cpu_percent(interval=0.1)

    approx_cpu_usage = (cpu_before + cpu_after) / 2

    # Print the measurement for the GitHub Actions log to capture
    print("\n--- MEASUREMENT ---")
    # Increased precision to capture tiny non-zero values
    print(f"Bubble Sort CPU Usage: {approx_cpu_usage:.4f}%")
    print("-------------------\n")


def test_quick(int_lists):
    """Verifies quick sort and measures runtime (Task 2b)."""

    # 1. FUNCTIONALITY CHECK
    for original_list in int_lists:
        assert is_sorted(quick(original_list))

    # 2. PERFORMANCE MEASUREMENT (Runtime)

    # Measure Runtime
    start_time = time.perf_counter()

    for _ in range(NUM_ITERATIONS):
        list_copy = PERFORMANCE_TEST_LIST[:]
        quick(list_copy)

    end_time = time.perf_counter()

    total_runtime = end_time - start_time

    # Calculate the average runtime per single sort
    runtime_per_sort = total_runtime / NUM_ITERATIONS

    # Print the measurement for the GitHub Actions log to capture
    print("\n--- MEASUREMENT ---")
    print(f"Quick Sort Runtime: {runtime_per_sort:.6f}s")
    print("-------------------\n")


def test_insertion(int_lists):
    # Verifies insertion sort and measures memory usage (Task 2c).

    # 1. FUNCTIONALITY CHECK
    for original_list in int_lists:
        assert is_sorted(insertion(original_list))

    # 2. PERFORMANCE MEASUREMENT (Memory Usage)

    # Clean up residual memory before measurement
    gc.collect()

    gc.disable()
    mem_before = CURRENT_PROCESS.memory_info().rss

    for _ in range(NUM_ITERATIONS):
        list_copy = PERFORMANCE_TEST_LIST[:]
        insertion(list_copy)

    mem_after = CURRENT_PROCESS.memory_info().rss

    gc.enable()

    # Calculate the memory difference (overhead) in megabytes
    memory_overhead_mb = (mem_after - mem_before) / (1024 * 1024)

    print("\n--- MEASUREMENT ---")
    print(f"Insertion Sort Memory Usage: {memory_overhead_mb:.6f} MB")
    print("-------------------\n")
