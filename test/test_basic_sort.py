import pytest
import numpy as np
import time
import psutil
import os
import random
from basic_sort_UNIQUE_SUFFIX.int_sort import bubble, quick, insertion

# --- CONSTANTS AND SETUP ---
LIST_SIZE = 50000
PERFORMANCE_TEST_LIST = [random.randint(1, 10000) for _ in range(LIST_SIZE)]
EXPECTED_SORTED = sorted(PERFORMANCE_TEST_LIST)
CURRENT_PROCESS = psutil.Process(os.getpid())


def is_sorted(int_list):
    # Testing oracle. Checks if a list of integers is sorted.

    return all(a <= b for a, b in zip(int_list, int_list[1:]))


@pytest.fixture
def int_lists():
    return [
        [3, 2, 1],
        [1, 1, 1],
        list(np.random.randint(low=-10, high=200, size=5)),
    ]


def test_bubble(int_lists):
    """Verifies bubble sort and measures CPU usage (Task 2a)."""

    # 1. FUNCTIONALITY CHECK
    for original_list in int_lists:
        assert bubble(original_list) == sorted(original_list)

    # 2. PERFORMANCE MEASUREMENT (CPU Usage)
    list_copy = PERFORMANCE_TEST_LIST[:]

    # Measure CPU Usage
    CURRENT_PROCESS.cpu_percent()  # Call once to prime
    time.sleep(0.01)
    cpu_before = CURRENT_PROCESS.cpu_percent()

    bubble(list_copy)

    cpu_after = CURRENT_PROCESS.cpu_percent(interval=0.1)
    approx_cpu_usage = (cpu_before + cpu_after) / 2

    # Print the measurement for the GitHub Actions log
    print("\n--- MEASUREMENT ---")
    print(f"Bubble Sort CPU Usage: {approx_cpu_usage:.2f}%")
    print("-------------------\n")


def test_quick(int_lists):
    """Verifies quick sort and measures runtime (Task 2b)."""

    # 1. FUNCTIONALITY CHECK
    for original_list in int_lists:
        assert quick(original_list) == sorted(original_list)

    # 2. PERFORMANCE MEASUREMENT (Runtime)
    list_copy = PERFORMANCE_TEST_LIST[:]

    # Measure Runtime
    start_time = time.perf_counter()
    quick(list_copy)
    end_time = time.perf_counter()

    runtime = end_time - start_time

    # Print the measurement for the GitHub Actions log
    print("\n--- MEASUREMENT ---")
    print(f"Quick Sort Runtime: {runtime:.6f}s")
    print("-------------------\n")


def test_insertion(int_lists):
    """Verifies insertion sort and measures memory usage (Task 2c)."""

    # 1. FUNCTIONALITY CHECK
    for original_list in int_lists:
        assert insertion(original_list) == sorted(original_list)

    # 2. PERFORMANCE MEASUREMENT (Memory Usage)
    list_copy = PERFORMANCE_TEST_LIST[:]

    # Measure Memory Usage (Resident Set Size - RSS)
    mem_before = CURRENT_PROCESS.memory_info().rss

    insertion(list_copy)

    mem_after = CURRENT_PROCESS.memory_info().rss

    # Calculate the memory difference (overhead) in megabytes
    memory_overhead_mb = (mem_after - mem_before) / (1024 * 1024)

    # Print the measurement for the GitHub Actions log
    print("\n--- MEASUREMENT ---")
    print(f"Insertion Sort Memory Usage: {memory_overhead_mb:.2f} MB")
    print("-------------------\n")
