"""
Eunhye Park
Project 4 - Hybrid Sorting - Solution Code
CSE 331 Spring 2022
"""

import gc
import time
from typing import TypeVar, List, Callable, Dict

T = TypeVar("T")  # represents generic type


# do_comparison is an optional helper function but HIGHLY recommended!!!
def do_comparison(first: T, second: T, comparator: Callable[[T, T], bool], descending: bool) -> bool:
    """
    Compare elements first and second and return `True` if `first` should come before `second`
    Takes custom comparator and whether the sort will be descending into account
    :param first: First value to compare
    :param second: Second value to compare
    :param comparator: Function which performs comparison
    :param descending: Determines whether comparison result should be flipped
    :return: True if first should come before second in a sorted list
    """
    return comparator(second, first) if descending else comparator(first, second)


def selection_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sort list using selection sort in-place using provided comparator
    :param data: list of items to be sorted
    :param comparator: function which takes two arguments of type T and returns True when the first argument should be treated as less than the second argument
    :param descending: bool indicating whether to sort in descending order (True) or not (False)
    """
    
    for i in range(len(data) - 1):
        #  find index of largest remaining element
        largest_index = i
        for j in range(i + 1, len(data)):
            compare = do_comparison(data[j], data[largest_index], comparator, descending)
            if compare:
                largest_index = j
        temp = data[i]
        data[i] = data[largest_index]
        data[largest_index] = temp

def bubble_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                descending: bool = False) -> None:
    """
    Sort list in-place using bubble sort
    :param data: list of items to be sorted
    :param comparator: function which takes two arguments of type T and returns True when the first argument should be treated as less than the second arguement
    :param descending: bool indicating whether to sort in descending order (True) or not (False)
    """
                
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if do_comparison(data[j + 1], data[j], comparator, descending):
                data[j], data[j+1] = data[j + 1], data[j]


def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sort list in-place using insertion sort
    :param data: list of items to be sorted
    :param comparator: function which takes two arguments of type T and returns True when the first argument should be treated as less than the second arguement
    :param descending: bool indicating whether to sort in descending order (True) or not (False)
    """

    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if do_comparison(data[j], data[j-1], comparator, descending):
                data[j-1], data[j] = data[j], data[j-1]
                

def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    Sort list in-place using merge sort and insertion sort algorithm
    :param data: list of items to be sorted
    :param threshold: maximum size at which insertion sort will be used instead of merge sort
    :param comparator: function which takes two arguments of type T and returns True when the first argument should
                       be treated as less than the second arguement
    :param descending: bool indicating whether to sort in descending order (True) or not (False)
    """
    sorted_list = [0]*len(data)
    
    def merge(left, mid, right) -> None:
    
        i, j, k = left, mid+1, left
        
        while(i <= mid and j <= right):
            if do_comparison(data[i], data[j], comparator, descending):
                sorted_list[k] = data[i]
                k += 1
                i += 1
            else:
                sorted_list[k] = data[j]
                k += 1
                j += 1
                
        
        if i > mid :
            for l in range(j, right+1):
                sorted_list[k] = data[l]
                k += 1

        else:
            for l in range(i, mid+1):
                sorted_list[k] = data[l]
                k += 1

        
        for l in range(left, right+1):
            data[l] = sorted_list[l]
        # inner function out        
    
    def sort(left, right):
        mid = int((left+right) / 2)
        
        if right - left + 1 <= threshold:
            for i in range(left, right+1):
                for j in range(i, 0, -1):
                    if do_comparison(data[j], data[j-1], comparator, descending):
                        data[j-1], data[j] = data[j], data[j-1]
                        
        elif left < right:
            sort(left, mid)
            sort(mid+1, right)
            merge(left, mid, right)
        
        
    
    sort(0, len(data)-1)
    
            

# A hybrid quicksort would be even faster but we don't want to give too much code away here!
def quicksort(data):
    """
    Sorts a list in place using quicksort
    :param data: Data to sort
    """

    def quicksort_inner(first, last):
        """
        Sorts portion of list at indices in interval [first, last] using quicksort

        :param first: first index of portion of data to sort
        :param last: last index of portion of data to sort
        """
        # List must already be sorted in this case
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)


def compare_times(algorithms: Dict[str, Callable[[List], None]], sizes: List[int], trials: int) \
        -> Dict[str, List[float]]:
    """
    return the average times in seconds required to run each algorithm on a list of each size
    :param algorithms: a dictionary whose values are callable sorting algorithm functions to consider,
                       and whose keys are names for the algorithms
    :param sizes: list of sizes of data to use in benchmark and every size should be used for every algorithm
    :param trials: number of trials to run each size/algorithm combination for
    :return: a dictionary whose keys are the keys of algorithms, and whose values are list of the
             average times it took to run those algorithms for different sizes, in the same order as param sizes
    """
    ret_dict = dict()
    for key in algorithms.keys():
        ret_dict[key] = []
        print(key)
        processing_time = 0.0
        for idx in range(trials):
            start = time.perf_counter()
            algorithms[key](sizes)
            ret_dict[key].append(time.perf_counter() - start)
    
    
    # print("Algorithm:", algorithms[algorithms.keys()]
    # print("Size     :", sizes)
    # print("trial    :", trials)
    
    return ret_dict


def plot_time_comparison():
    """
    Use compare_times to make a time comparison chart of the runtimes of different sorting algorithms.
    Requires matplotlib. Comment this out if you do not wish to install matplotlib.
    """
    import matplotlib.pyplot as plt

    algorithms = {
        "bubble": bubble_sort,
        "selection": selection_sort,
        "insertion": insertion_sort,
        "pure merge": lambda data: hybrid_merge_sort(data, threshold=0),
        "hybrid merge": hybrid_merge_sort,
    }
    sizes = [4, 5, 6, 7, 8, 9, 10, 25, 50, 100, 300, 500]
    trials = 75
    warmup_trials = 25

    compare_times(algorithms, sizes, warmup_trials)  # Warmup run, ignored
    gc.collect()  # Get this out of the way before the trials, might be overkill
    data = compare_times(algorithms, sizes, trials)

    plt.style.use('seaborn-colorblind')
    fig = plt.figure(figsize=(12, 8))
    axes = [
        plt.subplot2grid((2, 2), (0, 0)),
        plt.subplot2grid((2, 2), (0, 1)),
        plt.subplot2grid((2, 2), (1, 0), colspan=2),
    ]

    for algorithm in algorithms:
        # First plot shows abridged view to focus on smaller sizes
        axes[0].plot(sizes[:-2], data[algorithm][:-2], label=algorithm)
        axes[2].plot(sizes, data[algorithm], label=algorithm)
    for algorithm in ["pure merge", "hybrid merge"]:
        axes[1].plot(sizes, data[algorithm], label=algorithm)

    for ax in axes:
        ax.legend()
        ax.set_xlabel("Input Size")
        ax.set_ylabel("Time to Sort (sec)")
    axes[0].set_yscale("log")
    axes[0].set_title("Small Inputs, log y scale")
    axes[1].set_title("Larger Inputs, Pure vs Hybrid Merge")
    axes[2].set_title("Larger Inputs")
    fig.tight_layout()

    fig.show()


# Run the time comparison and make a plot
if __name__ == "__main__":
    plot_time_comparison()
