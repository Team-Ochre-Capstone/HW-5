# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================


# This module sorts lists of integers...


def bubble(int_list):

    # Sorts a list of integers using the bubble sort algorithm.

    # Args:
    #     int_list (list): The list of integers to be sorted.

    # Returns:
    # list: The list of integers sorted from int_list in ascending order.

    # Example:

    #     bubble([3, 4, 5, 2, 1, 1, 5])
    #     bubble sort[1, 1, 2, 3, 4, 5, 5]

    arr = int_list[:]  # Copy of original list
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):  # Traverse the list from 0 - n-
            if arr[j] > arr[j + 1]:  # Swap element if grater than next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("bubble sort")
    return arr


def quick(int_list):
    # Sorts a list of integers using the quicksort algorithm.

    # Args:
    #     int_list (list): The list of integers to be sorted.

    # Returns:
    # list: The list of integers sorted from int_list in ascending order.

    # Example:

    #     quick([3, 4, 5, 2, 1, 1, 5])
    #     quick sort[1, 1, 2, 3, 4, 5, 5]

    arr = int_list[:]  # Copy of original list

    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print("quick sort")
    return quick(left) + middle + quick(right)


def insertion(int_list):
    # Sorts a list of integers using the insertion sort algorithm.

    # Args:
    #     int_list (list): The list of integers to be sorted.

    # Returns:
    # list: The list of integers sorted from int_list in ascending order.

    # Example:

    #     bubble([3, 4, 5, 2, 1, 1, 5])
    #     insertion sort[1, 1, 2, 3, 4, 5, 5]

    arr = int_list[:]  # Copy of original list

    for i in range(1, len(arr)):
        key = arr[i]  # Element to be positioned
        j = i - 1

        # Shift elements of arr[0] - arr[i-1] that are greater than key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at after the element just smaller than it
        arr[j + 1] = key

    print("insertion sort")
    return arr
