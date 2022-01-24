from typing import TypeVar

from numpy import Inf          # For use in type hinting

# Type Declarations
T = TypeVar('T')        # generic type
SLL = TypeVar('SLL')    # forward declared
Node = TypeVar('Node')  # forward declare `Node` type


class SLLNode:
    """
    Node implementation
    Do not modify.
    """

    __slots__ = ['val', 'next']

    def __init__(self, value: T, next: Node = None) -> None:
        """
        Initialize an SLL Node
        :param value: value held by node
        :param next: reference to the next node in the SLL
        :return: None
        """
        self.val = value
        self.next = next

    def __str__(self) -> str:
        """
        Overloads `str()` method to casts nodes to strings
        return: string
        """
        return '(Node: ' + str(self.val) + ' )'

    def __repr__(self) -> str:
        """
        Overloads `repr()` method for use in debugging
        return: string
        """
        return '(Node: ' + str(self.val) + ' )'

    def __eq__(self, other: Node) -> bool:
        """
        Overloads `==` operator to compare nodes
        :param other: right operand of `==`
        :return: bool
        """
        return self.val == other.val if other is not None else False


class SinglyLinkedList:
    """
    Implementation of an SLL
    """

    __slots__ = ['head']

    def __init__(self) -> None:
        """
        Initializes an SLL
        :return: None
        DO NOT MODIFY THIS FUNCTION
        """
        self.head = None

    def __repr__(self) -> str:
        """
        Represents an SLL as a string
        DO NOT MODIFY THIS FUNCTION
        """
        return self.to_string()

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right hand operand of `==`
        :return: `True` if equal, else `False`
        DO NOT MODIFY THIS FUNCTION
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

    # ============ Modify below ============ #

    def to_string(self) -> str:
        """
        Converts an SLL to a string
        :return: string representation of the linked list
        """
        
        if self.head is None:
            return "None"
        
        ret_string = ""
        target_node = self.head
        
        while target_node is not None:
            ret_string += str(target_node.val)
            if target_node.next is not None:
                ret_string += " --> "
                
            target_node = target_node.next
                
        return ret_string
    
    def length(self) -> int:
        """
        Determines number of nodes in the list
        :return: number of nodes in list
        """
        
        target_node = self.head
        ret = 0
        if(target_node is None):
            return ret
        else:
            while target_node is not None:
                ret += 1
                target_node = target_node.next
            return ret
        
    def sum_list(self) -> T:
        """
        Sums the values in the list
        :return: sum of values in list
        """
        if self.head is None:
            return None
        
        ret = 0
        
        target_node = self.head
        while(target_node is not None):
            ret += target_node.val
            target_node = target_node.next
            
        return ret
    
    def push(self, value: T) -> None:
        """
        Pushes a SLLNode to the end of the list
        :param value: value to push to the list
        :return: None
        """
        
        new_node = SLLNode(value)
        
        if self.head is None:
            self.head = new_node
        elif self.head is not None:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            
            temp.next = new_node


    def remove(self, value: T) -> bool:
        """
        Removes the first node containing `value` from the SLL
        :param value: value to remove
        :return: bool whether or not deleted
        """
        
    
                

        pass

    def remove_all(self, value: T) -> bool:
        """
        Removes all instances of a node containing `value` from the SLL
        :param value: value to remove
        :return: bool whether any were deleted
        """

        pass

    def search(self, value: T) -> bool:
        """
        Searches the SLL for a node containing `value`
        :param value: value to search for
        :return: `True` if found, else `False`
        """
        
        target_node = self.head
        
        while target_node is not None:
            if target_node.val == value:
                return True
            target_node = target_node.next

        return False

    def count(self, value: T) -> int:
        """
        Returns the number of occurrences of `value` in this list
        :param value: value to count
        :return: number of time the value occurred
        """
        
        target_node = self.head
        ret = 0
        while target_node is not None:
            if target_node.val == value:
                ret += 1 
            target_node = target_node.next

        return ret
        

        pass


def max_crash_dist(data: SLL) -> int:
    """
    Figure out the furthest distance between two perfect square numbers, with none in between
    :return: int with the distance between, 0 if two or more perfect squares do not exist
    """

    target_node = data.head

    perfect_square = []
    
    print("*"*30)
    while target_node is not None:
        root_num = target_node.val ** 0.5
        print(target_node.val)
        if root_num == int(root_num):
            perfect_square.append(target_node.val)
                
        target_node = target_node.next

    perfect_square.sort()
    
    if len(perfect_square) < 2:
        return 0
    
    ret = 0
    
    for idx in range(1, len(perfect_square)):
        if ret < perfect_square[idx] - perfect_square[idx - 1]:
            ret = perfect_square[idx] - perfect_square[idx - 1]
            
    return ret