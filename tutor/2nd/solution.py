from os import remove
from typing import TypeVar, Tuple  # For use in type hinting

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


class RecursiveSinglyLinkedList:
    """
    Recursive implementation of an SLL
    """

    __slots__ = ['head', 'tail']

    def __init__(self) -> None:
        """
        Initializes an SLL
        :return: None
        """
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        """
        Represents an SLL as a string
        """
        return self.to_string(self.head)

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right hand operand of `==`
        :return: `True` if equal, else `False`
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

# ============ Modify below ============ #

    def to_string(self, curr: Node) -> str:
        """
        INSERT DOCSTRING HERE!
        Reference Project 1 for style/example
        """

        if self.head is None:
            return "None"
        
        if curr.next is not None:
            return str(curr.val) + " --> " + self.to_string(curr.next)
        elif curr is not None:
            return str(curr.val)


    def length(self, curr: Node) -> int:
        """
        INSERT DOCSTRING HERE!
        Reference Project 1 for style/example
        """
        
        if curr is None:
            return 0
        else:
            return self.length(curr.next) + 1
        
    def sum_list(self, curr: Node) -> T:
        """
        INSERT DOCSTRING HERE!
        Reference Project 1 for style/example
        """

        if self.head is None:
            return None
        
        elif curr.next is not None:
            return curr.val + self.sum_list(curr.next) 
        
        elif curr is not None:
            return curr.val
        
    def search(self, value: T) -> bool:
        """
        Searches the SLL for a node containing `value`
        :param value: value to search for
        :return: `True` if found, else `False`
        """

        def search_inner(curr: Node) -> bool:
            """
            INSERT DOCSTRING HERE!
            Reference Project 1 for style/example
            """
            if curr is None:
                return False
            
            if curr.val == value:
                return True
            else:
                return search_inner(curr.next)
            
            
        return search_inner(self.head)

    def count(self, value: T) -> int:
        """
        INSERT DOCSTRING HERE!
        Reference Project 1 for style/example
        """

        def count_inner(curr: Node) -> int:
            """
            INSERT DOCSTRING HERE!
            Reference Project 1 for style/example
            """
            if curr is None:
                return 0
            
            if curr.val == value:
                return count_inner(curr.next) + 1
            else:
                return count_inner(curr.next)
            
        return count_inner(self.head)

    def push(self, value: T, back: bool = True) -> None:
        """
        INSERT DOCSTRING HERE!
        Reference Project 1 for style/example
        """
        
        new_node = SLLNode(value)
        
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = self.head

        elif back is True:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = self.tail.next
            
        else:
            new_node.next = self.head
            self.head = new_node
        
    def remove(self, value: T) -> bool:
        """
        INSERT DOCSTRING HERE!
        Reference Project 1 for style/example
        """

        def remove_inner(curr: Node) -> Tuple[Node, bool]:
            """
            INSERT DOCSTRING HERE!
            Reference Project 1 for style/example
            """
            
            if curr is None:
                return curr, False
            
            if curr is self.head and curr.val == value:
                temp_node = curr
                self.head = self.head.next
                del temp_node
                
                if self.head is None:
                    self.tail = None
                    
                return self.head, True
            
            if curr.next.val == value:
                temp_node = curr.next
                curr.next = temp_node.next
                
                if temp_node == self.tail:
                    self.tail = curr

                del temp_node
                
                return curr, True

            else:
                return remove_inner(curr.next)
                                    
        return remove_inner(self.head)[1]

    def remove_all(self, value: T) -> bool:
        """
        INSERT DOCSTRING HERE!
        Reference Project 1 for style/example
        """
        
        def remove_all_inner(curr: Node) -> Tuple[Node, bool]:
            """
            INSERT DOCSTRING HERE!
            Reference Project 1 for style/example
            """
            ret_node, ret_bool = curr, False
            is_removed = False
            
            if curr is None:
                return curr, False
            
            if curr is self.head and curr.val == value:
                temp_node = self.head
                curr = curr.next
                self.head = curr
                is_removed = True
                
                del temp_node
                
                ret_node, ret_bool =  remove_all_inner(curr)
            
            elif curr.next is not None and curr.next.val == value:
                temp_node = curr.next
                curr.next = curr.next.next
                is_removed = True

                del temp_node
                
                if curr.next is None:
                    self.tail = curr.next
                
                ret_node, ret_bool =  remove_all_inner(curr)
                
            else:
                ret_node, ret_bool =  remove_all_inner(curr.next)
            
            
            if ret_bool:
                return ret_node, True
            else:
                return ret_node, is_removed
                            
        
        return remove_all_inner(self.head)[1]


def reverse_playlist(playlist: SLL, curr: Node) -> None:
    """
    INSERT DOCSTRING HERE!
    Reference Project 1 for style/example
    """

    if playlist.head is None:
        return None

    if curr.next is None:
        playlist.head = curr
    elif curr is not None:
        reverse_playlist(playlist, curr.next)
        playlist.tail.next = curr
        curr.next = None
        playlist.tail = curr
        