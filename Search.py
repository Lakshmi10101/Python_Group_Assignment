import time
import random
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


"""Module with the base implementation of a Search class."""

class Search(ABC):
    """Abstract base class for searching."""

    def __init__(self, items):
        if not isinstance(items, list):
            raise ValueError("Input must be a list.")
        if not all(isinstance(item, (int, float)) for item in items):
            raise ValueError("Input must be numbers.")
        self._items = items

    @abstractmethod
    def _search(self, value):
        """Returns the position of the searched element contained
        in the `_items` property.
        Returns:
            int: The position of the searched element.
        """
        pass

    def get_items(self):
        return self._items

    def _time(self, value):
        #self.time = 0
        start_time = time.time()
        pos = -1
        try:
            pos = self._search(value) 
                       # Call the method to search for the given input
        except Exception as e:
            print('Exception: ', e)
            raise e
        finally:
            end_time = time.time()
            self.time = end_time - start_time
            return pos, self.time
    
    
"""Module with the implementation of the BubbleSort algorithm."""

class LinearSearch(Search):
    """Class that represents a LinearSearch implementation."""

    def _search(self, value):
        # your code here
        items = self.get_items()
        N = len(items)

        for ind in range(N):
            if items[ind] == value:                
                return ind
        return -1

        
    def main(self, time_list):
        
        value = 1001
        
        # Call the sorting method and measure the time taken
        position, time_taken_searching = self._time(value)
        time_list.append(time_taken_searching)
        
        if position == -1:
            print('Element not found using Linear Search')
        else:
            print('Element ', value, 'found at index ', position, 'using Linear Search')


class BinarySearch(Search):
    """Class that represents a BinarySearch implementation."""
    def __init__(self, items):
      super().__init__(items)
      items = self.get_items()
      try:
        if not self._is_sorted(items):
              raise ValueError("Input list must be sorted in ascending order.")
      except ValueError as val_err:
        print('ValueError', val_err)
        self._items = sorted(items) 

    def _is_sorted(self, items):
        # Helper method to check if a list is sorted in ascending order
        N = len(items)
        return all(items[i] <= items[i + 1] for i in range(N - 1))

    def _search(self, value):
        # your code here
        items = self.get_items()
        N = len(items)
        
        low_pos = 0
        high_pos = N - 1
        while low_pos <= high_pos:
          mid_pos = (low_pos + high_pos) // 2 
          if items[mid_pos] == value:            # Checking for value in mid_pos
            return mid_pos
          elif items[mid_pos] < value:        
            low_pos = mid_pos + 1                # Update low_pos to reduce search space
          else:
            high_pos = mid_pos - 1                # Update high_pos to reduce search space
    
        return -1

        
    def main(self, time_list):
        
        value  = 1001

        # Call the sorting method and measure the time taken
        position, time_taken_searching = self._time(value)
        time_list.append(time_taken_searching)
        
        # Retrieve the sorted list
        sorted_arr = self.get_items()
        
        if position == -1:
            print('Element not found using Binary Search')
        else:
            print('Element ', value, 'found at index ', position, 'using Binary Search')
        
def plot_execution_time():
    # To plot the execution time V/s size of input data
    plt.plot(size, linear_time, label = 'Linear Search')
    plt.plot(size, binary_time, label = 'Binary Search')
    plt.xlabel('Size of Data')
    plt.ylabel('Execution time (in seconds)')
    plt.title('Time graph for Searching')
    plt.legend()
    plt.savefig('search_time.png')
    plt.show()

if __name__ == "__main__":
    size = [1000, 5000, 10000, 50000, 100000]
    linear_time = []
    binary_time = []
    for size_value in size:
        input_list = random.sample(range(0, size_value), size_value)
        print('Size of array:', size_value)
            
        # Create an instance of LinearSearch
        LinearSearch(input_list).main(linear_time)
        # Create an instance of BinarySearch
        BinarySearch(input_list).main(binary_time)
        print('----------------------------------------------------------')
    
    plot_execution_time()
                
    
