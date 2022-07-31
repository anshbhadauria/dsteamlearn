# test methods of binary search
import time
from collections.abc import Callable
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.ERROR)


def binary_search_recursive(sorted_array: list, k: int, start: int, end: int) -> int:
    """
    This is the recursive implementation of binary_search.
    Args:
        sorted_array: a sorted array
        k: element we are looking for
        start: from which index of sorted_array
        end: to which index of sorted_array
    Returns:
        Index of sorted_array where "k" was found.
    """
    if end >= start:
        mid_index = (start + end) // 2
        LOGGER.debug(f"start {start}, end {end}, mid {mid_index} searching {k} found {sorted_array[mid_index]}")
        if k == sorted_array[mid_index]:
            LOGGER.debug(f"The element {k} was found at index {mid_index}")
            return mid_index
        if k > sorted_array[mid_index]:
            return binary_search_recursive(sorted_array, k, start=mid_index + 1, end=len(sorted_array) - 1)
        if k < sorted_array[mid_index]:
            return binary_search_recursive(sorted_array, k, start=0, end=mid_index - 1)
    else:
        LOGGER.debug(f"The element {k} was not found.")
        return -1


def binary_search_iter(sorted_array: list, k: int, start: int, end: int) -> int:
    """
    This is the iterative implementation of binary_search.
    Args:
        sorted_array: a sorted array
        k: element we are looking for
        start: from which index of sorted_array
        end: to which index of sorted_array
    Returns:
        Index of sorted_array where "k" was found.
    """
    while start <= end:
        mid_index = (start + end) // 2
        LOGGER.debug(f"start {start}, end {end}, mid {mid_index} searching {k} found {sorted_array[mid_index]}")
        if sorted_array[mid_index] == k:
            LOGGER.debug(f"The element {k} was found at index {mid_index}")
            return mid_index
        if k > sorted_array[mid_index]:
            start = mid_index + 1
        if k < sorted_array[mid_index]:
            end = mid_index - 1
    LOGGER.debug(f"The element {k} was not found.")
    return -1


def test_and_time(binary_function: Callable) -> float:
    """ Function to test and calculate time of execution
    Args:
        binary_function: name of the binary search function
    Returns:
        time in seconds for execution
    """
    start_time_bin_search = time.time()
    sorted_arr_1 = [1, 2, 3, 4, 5, 6, 7, 9, 10, 13, 14, 16, 19, 21, 33]
    sorted_arr_2 = list(range(1, 1_000_000))
    assert binary_function(sorted_array=sorted_arr_1, k=33, start=0, end=len(sorted_arr_1) - 1) == 14
    assert binary_function(sorted_array=sorted_arr_1, k=55, start=0, end=len(sorted_arr_1) - 1) == -1
    assert binary_function(sorted_array=[1], k=1, start=0, end=0) == 0
    assert binary_function(sorted_array=sorted_arr_2, k=1, start=0, end=len(sorted_arr_1) - 2) == 0
    return time.time() - start_time_bin_search


if __name__ == "__main__":
    iteration_count = 100
    binary_search_avg = sum(test_and_time(binary_search_recursive) for _ in range(iteration_count))/ iteration_count
    binary_search__iter_avg = sum(test_and_time(binary_search_iter) for _ in range(iteration_count)) / iteration_count
    print(f"Average time of execution for binary_search_recursive is {binary_search_avg}")  # 0.0115 seconds
    print(f"Time of execution for binary_search_iter is {binary_search__iter_avg}")  # 0.0112 seconds
