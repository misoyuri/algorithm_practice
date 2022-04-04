"""
Ian Barber,Alex Woodring, Max Huang, and Angelo Savich
Project 8 - Heaps - Solution Code
CSE 331 Spring 2022

"""
from typing import List, Tuple, Any


class MinHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = []

    def __str__(self) -> str:
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data)

    __repr__ = __str__

    def to_tree_format_string(self) -> str:
        """
        Prints heap in Breadth First Ordering Format
        :return: String to print
        """
        string = ""
        # level spacing - init
        nodes_on_level = 0
        level_limit = 1
        spaces = 10 * int(1 + len(self))

        for i in range(len(self)):
            space = spaces // level_limit
            # determine spacing

            # add node to str and add spacing
            string += str(self.data[i]).center(space, ' ')

            # check if moving to next level
            nodes_on_level += 1
            if nodes_on_level == level_limit:
                string += '\n'
                level_limit *= 2
                nodes_on_level = 0
            i += 1

        return string

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def __len__(self) -> int:
        """
            DOC STRING GOES HERE
        """
        return len(self.data)
        
        
    def empty(self) -> bool:
        """
            DOC STRING GOES HERE
        """
        return len(self.data) == 0

    def top(self) -> int:
        """
            DOC STRING GOES HERE
        """
        if self.empty():
            return None
        else:
            return self.data[0]

    def get_left_child_index(self, index: int) -> int:
        """
            DOC STRING GOES HERE
        """
        left_child_index = index * 2 + 1
        
        if len(self.data) > left_child_index:
            return left_child_index
        else:
            return None

    def get_right_child_index(self, index: int) -> int:
        """
            DOC STRING GOES HERE
        """
        right_child_index = index * 2 + 2
            
        if len(self.data) > right_child_index:
            return right_child_index
        else:
            return None

    def get_parent_index(self, index) -> int:
        """
            DOC STRING GOES HERE
        """
        if index == 0:
            return None
        else:
            return int((index - 1) / 2)
        

    def get_min_child_index(self, index: int) -> int:
        """
            DOC STRING GOES HERE
        """
        left_child_index = self.get_left_child_index(index)
        right_child_index = self.get_right_child_index(index)
        
        if left_child_index is None:
            return None
        elif right_child_index is None:
            return left_child_index
        else:
            if self.data[left_child_index] < self.data[right_child_index]:
                return left_child_index
            else:
                return right_child_index
        
    def percolate_up(self, index: int) -> None:
        """
            DOC STRING GOES HERE
        """
        while index != 0 and self.data[self.get_parent_index(index)] > self.data[index]:
            self.data[self.get_parent_index(index)], self.data[index] = self.data[index], self.data[self.get_parent_index(index)]
            index = self.get_parent_index(index)
            
    def percolate_down(self, index: int) -> None:
        """
            DOC STRING GOES HERE
        """
        while True:
            min_child_pos = self.get_min_child_index(index)
            if min_child_pos is None:
                break
        
            if self.data[min_child_pos] < self.data[index]:
                self.data[min_child_pos], self.data[index] = self.data[index], self.data[min_child_pos]
                index = min_child_pos
            else:
                break


    def push(self, val: int) -> None:
        """
            DOC STRING GOES HERE
        """
        self.data.append(val)
        self.percolate_up(len(self.data) - 1)        

    def pop(self) -> int:
        """
            DOC STRING GOES HERE
        """
        poped_element = self.data[0]
        
        self.data[0], self.data[len(self.data) - 1] = self.data[len(self.data) - 1], self.data[0]
        self.data.pop()
        
        self.percolate_down(0)
        
        return poped_element


class MaxHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = MinHeap()

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data.data)

    __repr__ = __str__

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self.data)

    def print_tree_format(self):
        """
        Prints heap in bfs format
        """
        self.data.to_tree_format_string()

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def empty(self) -> bool:
        """
            DOC STRING GOES HERE
        """
        return self.data.empty()

    def top(self) -> int:
        """
            DOC STRING GOES HERE
        """
        top_value = self.data.top() 
        
        if top_value is None:
            return None
        else:
            return -top_value
        
    def push(self, key: int) -> None:
        """
            DOC STRING GOES HERE
        """
        self.data.push(-key)

    def pop(self) -> int:
        """
            DOC STRING GOES HERE
        """
        return -self.data.pop()


def current_medians(values) -> List[int]:
    """
        DOC STRING GOES HERE
    """
    min_heap = MinHeap()
    max_heap = MaxHeap()
    median_list = []
    for value in values:
        if max_heap.empty() or max_heap.top() >= value:
            max_heap.push(value);
        else:
            min_heap.push(value);
            
        if len(max_heap) > len(min_heap) + 1:
            min_heap.push(max_heap.pop());
            
        elif len(max_heap) < len(min_heap):
            max_heap.push(min_heap.pop());



        if len(max_heap) == len(min_heap):
            median_list.append((max_heap.top() + min_heap.top())/2)
            
        elif len(max_heap) > len(min_heap):
            median_list.append(max_heap.top())
            
        else:
            median_list.append(min_heap.top())
        
    return median_list