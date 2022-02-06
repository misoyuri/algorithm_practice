"""
Project 3 Starter
CSE 331 S22 (Onsay)
Matt Kight & Lukas Richters
Original authors: Andrew McDonald, Alex Woodring & Andrew Haas
DLL.py
"""

from typing import TypeVar, List

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)


# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    Do not modify.
    """
    __slots__ = ["value", "next", "prev", "child"]

    def __init__(self, value: T, next: Node = None, prev: Node = None, child: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        """
        self.next = next
        self.prev = prev
        self.value = value

        # The child attribute is only used for the application problem
        self.child = child

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    # MODIFY BELOW #

    def empty(self) -> bool:
        """
        checks to see whether the doubly linked list is empty or not
        :return: True if list is empty, False otherwise
        """
        if self.head is None:
            return True

        return False

    def push(self, val: T, back: bool = True) -> None:
        """
        adds a node containing the value to the back (or front if False) of doubly linked list and updates the size
        :param value: value to add to the list, bool indicating whether to add to the back of the doubly linked list
        """
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        elif back is True:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
        else:
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.size += 1

    def pop(self, back: bool = True) -> None:
        """
        removes a node from the back (or front if False) of doubly linked list and update the size accordingly
        :param value: bool indicating whether to remove from the back of the doubly linked list
        """

        if self.head is None:
            return None
        
        elif self.head == self.tail:
            self.head = self.tail = None
        
        elif back is True:
            self.tail.prev.next = self.tail.next
            self.tail = self.tail.prev
        else:
            self.head.next.prev = None
            self.head = self.head.next
        
        self.size -= 1

    def list_to_dll(self, source: List[T]) -> None:
        """
        create a doubly linked list from a standard Python list
        :param value: Python list
        """
    
        for val in source:
            self.push(val)

        return None

    def dll_to_list(self) -> List[T]:
        """
        create a standard Python list from a doubly linked list
        :return: Python list
        """
        curr_node = self.head
        ret_list = []
        while curr_node is not None:
            ret_list.append(curr_node.value)
            curr_node = curr_node.next
            
        return ret_list


    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        constructs list of node with the value in doubly linked list
        :param value: value to be found in doubly linked list, and bool indicating whether to find first element in DLL (True) or else find all elements
        :return: associated node object list whose value is val, return empty if value does not exist
        """
        pass

    def find(self, val: T) -> Node:
        """
        finds first node with value in doubly linked list
        :param value: value to be found in doubly linked list
        :return: first node object in doubly linked list whose value is val
        """
        curr_node = self.head
        
        while curr_node is not None:
            if curr_node.value == val:
                return curr_node
            
            curr_node = curr_node.next

        return None
    
    def find_all(self, val: T) -> List[Node]:
        """
        finds all nodes with value in doubly linked list
        :param value: value to be found in doubly linked list
        :return: standard Python list of all node objects in doubly linked list whose value is val
        """
        curr_node = self.head
        ret_list = []
        
        while curr_node is not None:
            if curr_node.value == val:
                ret_list.append(curr_node)
            curr_node = curr_node.next

        return ret_list

    def _remove_node(self, to_remove: Node) -> None:
        """
        remove a given node
        :param value: node to be removed
        """
        if self.head is None:
            return None
        
        elif self.head == self.tail:
            self.head = self.tail = None
            
        elif self.head == to_remove:
            self.pop(False)
            
        elif self.tail == to_remove:
            self.pop(True)
            
        else:
            to_remove.prev.next = to_remove.next
            to_remove.next.prev = to_remove.prev
        
    def remove(self, val: T) -> bool:
        """
        removes the first node with the value in doubly linked list
        :param value: value to be removed from doubly linked list
        :return: bool indicating whether a node was found and removed
        MUST CALL _REMOVE_NODE
        """
        curr_node = self.head
        
        while curr_node is not None:
            if curr_node.value == val:
                self._remove_node(curr_node)
                return True
            
            else:
                curr_node = curr_node.next

        return False

    def remove_all(self, val: T) -> int:
        """
        removes all nodes with the value in doubly linked list
        :param value: value to be removed from doubly linked list
        :return: number of node objects with value removed from doubly linked list
        MUST CALL _REMOVE_NODE
        """
        removed = 0
        return removed

    def reverse(self) -> None:
        """
        reverses doubly linked list in-place
        """
        pass


def secretary_scheduler(dll: DLL) -> DLL:
    """
    turns a multilevel doubly linked list into a single level doubly linked list
    :param value: a doubly linked list where each node holds a value of str as well as a child
    :return: doubly linked list holding str representing the names of all the tasks
    """
    pass
