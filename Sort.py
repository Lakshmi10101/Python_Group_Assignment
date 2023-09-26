import time
import random
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


"""Module with the base implementation of a Sort class."""

class Sort(ABC):
    """Abstract base class for sorting."""

    def __init__(self, items):
        if not isinstance(items, list):
            raise ValueError("Input must be a list.")
        self._items = items

    @abstractmethod
    def _sort(self, items):
        """Returns the sorted version of the elements contained
        in the `_items` property.
        Returns:
            List: The sorted elements.
        """
        pass

    def get_items(self):
        return self._items

    def _time(self):
        start_time = time.time()
        try:
            self._sort(self._items)             # Call the method to sort the given input
        except Exception as e:
            print('Exception: ', e)
            raise e
        finally:
            end_time = time.time()
            self.time = end_time - start_time
            return self.time
    
    
"""Module with the implementation of the MergeSort algorithm."""

class MergeSort(Sort):
    """Class that represents a MergeSort implementation."""

    def _sort(self, items):
        # your code here
        try:
            sorted_items = self._merge_sort(items)
        except Exception as e:
            print('Exception: ', e)
            raise e
        else:
            self._items = sorted_items
    
    def _merge_sort(self, items):
        N = len(items)

        mid_index = N//2                # Finding the middle index of the list
        # Splitting the list into two halves
        left_half = items[:mid_index]
        right_half = items[mid_index:]
        
        # Recursively sorting the first half using MergeSort
        if len(left_half) > 1: 
            left_half = self._merge_sort(left_half) 
            
        # Recursively sorting the second half using MergeSort
        if len(right_half) > 1:
            right_half = self._merge_sort(right_half)      
        
        # Merging the sorted haves in order
        sorted_items = self._merge(left_half, right_half)  
        
        return sorted_items

    def _merge(self, left, right):
        # your code here
        merged = []
        left_ind = 0
        right_ind = 0

        left_len = len(left)
        right_len = len(right)

        # Combining data from two lists in ascending order
        while left_ind < left_len and right_ind < right_len:
          if left[left_ind] < right[right_ind]:
              merged.append(left[left_ind])
              left_ind += 1
          else:
              merged.append(right[right_ind])
              right_ind += 1
        
        # To account for any element left behind
        merged.extend(left[left_ind:])
        merged.extend(right[right_ind:])
        
        return merged
        
    def main(self, time_list):
        
        # Call the sorting method and measure the time taken
        time_taken_sorting = self._time()
        time_list.append(time_taken_sorting)
        
        # Retrieve the sorted list
        sorted_arr = self.get_items()        
        #print("Sorted array:", sorted_arr)
        
        print("Time taken for sorting using Merge Sort:", time_taken_sorting, "seconds")


# Driver Code
if __name__ == "__main__":
    size = [1000, 5000, 10000, 50000, 100000]
    merge_time = []
    for size_value in size:
        input_list = random.sample(range(0, size_value), size_value)
        print('Size of array:', size_value)
            
        # Create an instance of MergeSort
        MergeSort(input_list).main(merge_time)
