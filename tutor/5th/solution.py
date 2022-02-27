"""
CSE331 Project 5 SS'22
Circular Double-Ended Queue
Jacob Caurdy, Andrew Haas
starter.py
"""
from typing import TypeVar, List
from random import randint, shuffle
from timeit import default_timer
# from matplotlib import pyplot as plt # COMMENT OUT THIS LINE (and `plot_speed`) if you don't want matplotlib
import gc

T = TypeVar('T')


class CircularDeque:
    """
    Representation of a Circular Deque using an underlying python list
    """

    __slots__ = ['capacity', 'size', 'queue', 'front', 'back']

    def __init__(self, data: List[T] = None, front: int = 0, capacity: int = 4):
        """
        Initializes an instance of a CircularDeque
        :param data: starting data to add to the deque, for testing purposes
        :param front: where to begin the insertions, for testing purposes
        :param capacity: number of slots in the Deque
        """
        if data is None and front != 0:
            data = ['Start']  # front will get set to 0 by front_enqueue if the initial data is empty
        elif data is None:
            data = []

        self.capacity: int = capacity
        self.size    : int = len(data)
        self.queue   : List[T] = [None] * capacity
        self.back    : int = None if not data else self.size + front - 1
        self.front   : int = front if data else None

        for index, value in enumerate(data):
            self.queue[index + front] = value

    def __str__(self) -> str:
        """
        Provides a string representation of a CircularDeque
        'F' indicates front value
        'B' indicates back value
        :return: the instance as a string
        """
        if self.size == 0:
            return "CircularDeque <empty>"

        str_list = [f"CircularDeque <"]
        for i in range(self.capacity):
            str_list.append(f"{self.queue[i]}")
            if i == self.front:
                str_list.append('(F)')
            elif i == self.back:
                str_list.append('(B)')
            if i < self.capacity - 1:
                str_list.append(',')

        str_list.append(">")
        return "".join(str_list)

    __repr__ = __str__

    #============ Modifiy Functions Below ============#

    def __len__(self) -> int:
        """
        FILL OUT DOCSTRINGS
        """
        return self.size 

    def is_empty(self) -> bool:
        """
        FILL OUT DOCSTRINGS
        """
        return self.size == 0
    
    def front_element(self) -> T:
        """
        FILL OUT DOCSTRINGS
        """
        if self.front is not None:
            return self.queue[self.front]
        else:
            return self.front
    
    def back_element(self) -> T:
        """
        FILL OUT DOCSTRINGS
        """
        if self.back is not None:
            return self.queue[self.back]
        else:
            return self.back

    def grow(self) -> None:
        """
        FILL OUT DOCSTRINGS
        """
        new_q = [None] * (self.capacity * 2)
        new_q_back = 0
        
        if self.size != 0:
            while new_q_back < self.size:
                new_q[new_q_back] = self.queue[self.front]
                self.front = (self.front + 1) % self.capacity
                new_q_back += 1
        
        self.queue = new_q
        self.front = 0
        self.back = new_q_back - 1
        self.capacity *= 2

        return None
    
    def shrink(self) -> None:
        """
        FILL OUT DOCSTRINGS
        """
        if self.capacity <= 4:
            return None
        
        new_q = [None] * int(self.capacity / 2)
        new_q_back = 0
        
        if self.size != 0:
            while new_q_back < self.size:
                new_q[new_q_back] = self.queue[self.front]
                self.front = (self.front + 1) % self.capacity
                new_q_back += 1
        
        self.queue = new_q
        self.front = 0
        self.back = new_q_back - 1
        self.capacity = int(self.capacity / 2)

    def enqueue(self, value: T, front : bool = True) -> None:
        """
        FILL OUT DOCSTRINGS
        """
        
        
        if self.size == 0:
            self.front = self.back = 0
            self.queue[0] = value
        
        elif front:
            self.front -= 1
            if self.front < 0:
                self.front += self.capacity
            
            self.queue[self.front] = value
        
        else:
            self.back = (self.back + 1) % self.capacity
            
            self.queue[self.back] = value
            
        self.size += 1
        
        if self.size == self.capacity:
            self.grow()

    def dequeue(self, front : bool = True) -> T:
        """
        FILL OUT DOCSTRINGS
        """
        if self.size == 0:
            return None
        
        poped_element = None
        
        if front:
            # self.queue[self.front], poped_element = None, self.queue[self.front]
            poped_element = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            
        else:
            # self.queue[self.back], poped_element = None, self.queue[self.back]
            poped_element = self.queue[self.back]
            self.back = (self.back - 1 + self.capacity) if self.back - 1 < 0 else (self.back - 1)
        
        self.size -= 1
        
        if self.size <= int(self.capacity / 4) and int(self.capacity / 2) >=4 :
            self.shrink()
        
        return poped_element




class CDLLNode:
    """
    Node for the CDLL
    """

    __slots__ = ['val', 'next', 'prev']

    def __init__(self, val: T, next: 'CDLLNode' = None, prev: 'CDLLNode' = None) -> None:
        """
        Creates a CDLL node
        :param val: value stored by the next
        :param next: the next node in the list
        :param prev: the previous node in the list
        :return: None
        """
        self.val, self.next, self.prev = val, next, prev

    def __eq__(self, other: 'CDLLNode') -> bool:
        """
        Compares two CDLLNodes by value
        :param other: The other node
        :return: true if comparison is true, else false
        """
        return self.val == other.val

    def __str__(self) -> str:
        """
        Returns a string representation of the node
        :return: string
        """
        return "<= (" + str(self.val) + ") =>"

    __repr__ = __str__


class CDLL:
    """
    A (C)ircular (D)oubly (L)inked (L)ist
    """

    __slots__ = ['head', 'size']

    def __init__(self) -> None:
        """
        Creates a CDLL
        :return: None
        """
        self.size = 0

    def __eq__(self, other: 'CDLL') -> bool:
        """
        Compares two CDLLs by value
        :param other: the other CDLL
        :return: true if comparison is true, else false
        """
        n1: CDLLNode = self.head
        n2: CDLLNode = other.head
        for _ in range(self.size):
            if n1 != n2: return False
            n1, n2 = n1.next, n2.next
        return True

    def __str__(self) -> str:
        """
        :return: a string representation of the CDLL
        """
        n1: CDLLNode = self.head
        joinable: List[str] = []
        while n1 is not self.head:
            joinable.append(str(n1))
            n1 = n1.next
        return ''.join(joinable)

    __repr__ = __str__

    def insert(self, val: T, front: bool = True) -> None:
        """
        inserts a node with val `val` in the front or back
        :param val: value to insert
        :param front: boolean indicator to insert in front or back
        :return: None
        """
        if not self.size:
            self.head = CDLLNode(val)
        elif self.size == 1:
            self.head.prev = self.head.next = CDLLNode(val, self.head, self.head)

        # now the front/back distinction starts to matter

        elif front:
            self.head.next = CDLLNode(val, self.head.next, self.head)
            self.head.next.next.prev = self.head.next
        else:
            self.head.prev = CDLLNode(val, self.head, self.head.prev)
            self.head.prev.prev.next = self.head.prev

        self.size += 1

    def remove(self, front: bool = True) -> None:
        """
        removes a node
        :param front: boolean indicator of whether to remove the front node or the tail node
        :return: None
        """
        if not self.size:
            return
        elif self.size == 1:
            self.head = None

        # now front/back distinction starts to matter

        elif front:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        else:
            self.head.prev = self.head.prev.prev
            self.head.prev.next = self.head

        self.size -= 1


class CDLLCD:
    """
    (C)ircular (D)oubly (L)inked (L)ist (C)ircular (D)equeue
    This is essentially just an interface for the above
    """

    def __init__(self) -> None:
        """
        FILL OUT DOCSTRINGS
        """
        self.CDLL: CDLL = CDLL()

        """
        You may have additional member variables - they go here
        """

    def __eq__(self, other: 'CDLLCD') -> bool:
        """
        Compares two CDLLCDs by value
        :param other: the other CDLLCD
        :return: true if equal, else false
        """
        return self.CDLL == other.CDLL

    def __str__(self) -> str:
        """
        :return: string representation of the CDLLCD
        """
        return str(self.CDLL)

    __repr__ = __str__

    def enqueue(self, val: T, front: bool = True) -> None:
        """
        FILL
        """
        pass

    def dequeue(self, front: bool = True) -> T:
        """
        FILL
        """
        pass


def plot_speed():
    """
    Compares performance of the CDLLCD and the standard array based deque
    """

    # First we'll test sequences of basic operations

    sizes = [100*i for i in range(0,200,5)]

    # (1) Grow large
    grow_avgs_array = []
    grow_avgs_CDLL  = []

    for size in sizes:
        grow_avgs_array.append(0)
        grow_avgs_CDLL.append(0)
        data = list(range(size))
        for trial in range(3):

            gc.collect() # What happens if you remove this? Hint: memory fragmention
            cd_array = CircularDeque()
            cd_DLL   = CDLLCD()

            # randomize data
            shuffle(data)

            start = default_timer()
            for item in data:
                cd_array.enqueue(item, item % 2)
            grow_avgs_array[-1] += (default_timer() - start)/3

            start = default_timer()
            for item in data:
                cd_DLL.enqueue(item, item % 2)
            grow_avgs_CDLL[-1] += (default_timer() - start)/3

    plt.plot(sizes, grow_avgs_array, color = 'blue', label = 'Array')
    plt.plot(sizes, grow_avgs_CDLL, color = 'red', label = 'CDLL')
    plt.title("Enqueue and Grow")
    plt.legend(loc = 'best')
    plt.show()

    # (2) Grow Large then Shrink to zero

    shrink_avgs_array = []
    shrink_avgs_CDLL  = []

    for size in sizes:
        shrink_avgs_array.append(0)
        shrink_avgs_CDLL.append(0)
        data = list(range(size))

        for trial in range(3):

            gc.collect()
            cd_array = CircularDeque()
            cd_DLL   = CDLLCD()

            # randomize data
            shuffle(data)

            start = default_timer()
            for item in data:
                cd_array.enqueue(item, item % 2)
            for item in data:
                cd_array.dequeue(not item % 2)
            shrink_avgs_array[-1] += (default_timer() - start)/3

            start = default_timer()
            for item in data:
                cd_DLL.enqueue(item, item % 2)
            for item in data:
                cd_DLL.dequeue(not item % 2)
            shrink_avgs_CDLL[-1] += (default_timer() - start)/3

    plt.plot(sizes, shrink_avgs_array, color = 'blue', label = 'Array')
    plt.plot(sizes, shrink_avgs_CDLL, color = 'red', label = 'CDLL')
    plt.title("Enqueue, Grow, Dequeue, Shrink")
    plt.legend(loc = 'best')
    plt.show()

    # (3) Test with random operations

    random_avgs_array = []
    random_avgs_CDLL  = []

    for size in sizes:
        random_avgs_array.append(0)
        random_avgs_CDLL.append(0)
        data = list(range(size))

        for trial in range(3):

            gc.collect()
            cd_array = CircularDeque()
            cd_DLL   = CDLLCD()

            shuffle(data)

            start = default_timer()
            for item in data:
                if randint(0,3) <= 2:
                    cd_array.enqueue(item, item % 2)
                else:
                    cd_array.dequeue(item % 2)
            random_avgs_array[-1] += (default_timer() - start)/3

            start = default_timer()
            for item in data:
                if randint(0,3) <= 2:
                    cd_DLL.enqueue(item, item % 2)
                else:
                    cd_DLL.dequeue(item % 2)
            random_avgs_CDLL[-1] += (default_timer() - start)/3

    plt.plot(sizes, random_avgs_array, color = 'blue', label = 'Array')
    plt.plot(sizes, random_avgs_CDLL, color = 'red', label = 'CDLL')
    plt.title("Operations in Random Order")
    plt.legend(loc = 'best')
    plt.show()

    def max_len_subarray(data, bound, structure):
        """
        returns the length of the largest subarray of `data` with sum less or eq to than `bound`
        :param data: list of integers to operate on
        :param bound: largest allowable sum
        :param structure: either a CircularDeque or a CDLLCD
        :return: the length
        """
        index, max_len, subarray_sum = 0, 0, 0
        while index < len(data):

            while subarray_sum <= bound and index < len(data):
                structure.enqueue(data[index])
                subarray_sum += data[index]
                index += 1
            max_len = max(max_len, subarray_sum)

            while subarray_sum > bound:
                subarray_sum -= structure.dequeue(False)

        return max_len

    # (4) A common application

    application_avgs_array = []
    application_avgs_CDLL = []

    data = [randint(0,1) for i in range(5000)]
    window_lengths = list(range(0,200,5))

    for length in window_lengths:
        application_avgs_array.append(0)
        application_avgs_CDLL.append(0)

        for trial in range(3):

            gc.collect()
            cd_array = CircularDeque()
            cd_DLL   = CDLLCD()

            start = default_timer()
            max_len_subarray(data, length, cd_array)
            application_avgs_array[-1] += (default_timer() - start)/3

            start = default_timer()
            max_len_subarray(data, length, cd_DLL)
            application_avgs_CDLL[-1] += (default_timer() - start)/3

    plt.plot(window_lengths, application_avgs_array, color = 'blue', label = 'Array')
    plt.plot(window_lengths, application_avgs_CDLL, color = 'red', label = 'CDLL')
    plt.title("Sliding Window Application")
    plt.legend(loc = 'best')
    plt.show()
