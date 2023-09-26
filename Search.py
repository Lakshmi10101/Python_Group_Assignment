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
    


if __name__ == "__main__":
    size = [1000, 5000, 10000, 50000, 100000]
    linear_time = []
    for size_value in size:
        input_list = random.sample(range(0, size_value), size_value)
        print('Size of array:', size_value)
            
        # Create an instance of LinearSearch
        LinearSearch(input_list).main(linear_time)
                
    