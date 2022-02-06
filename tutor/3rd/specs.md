# Project 3: Doubly Linked Lists

**Due: Thursday, February 10th @ 10:00PM ET**

*This is not a team project. Do not copy someone else’s work.*

# Assignment Overview

Doubly linked lists (DLLs) are a fundamental data structure used to store sequential information. DLLs consist of a chain of *nodes* linked to one another by *forward* and *backward* references, such that one may traverse the chain from the *head* to the *tail*, or vice-versa. Each node stores a *value*, which may be a number, string, or more complex object.

![](img/basic_DLL.png)
Traditional *arrays* provide a simpler means for storing sequential information, but come with a major drawback which DLLs avoid: arrays require contiguous blocks of memory, while DLLs may utilize memory wherever it is available. In settings where data is updated, manipulated or deleted frequently, DLLs outperform traditional arrays by avoiding the need for memory reallocation. [This article](https://www.geeksforgeeks.org/linked-list-vs-array/) gives a nice overview of the distinction between DLLs and arrays.

Also see [Zybooks](https://learn.zybooks.com/zybook/MSUCSE331OnsayFall2021/chapter/19/section/5) if you need further review of DLL. 


# Assignment Notes

1. Time **and** space complexity account for 30% of the points on Project 3. Be sure to review the rubric and adhere to complexity requirements!
2. Docstrings (the multi-line comments beneath each function header) are NOT provided in Project 3 and will need to be completed for full credit.
3. To evaluate your code's running time, utilize the test\_cProfile function in the tests.py file. This will be a powerful tool for you to utilize throughout CSE 331 and beyond when runtime is of the essence. More information is available in the [official Python documentation](https://docs.python.org/3/library/profile.html).
4. Testcases are your friend: before asking about the form of input/output or what happens in a particular edge case, check to see if the testcases answer your question for you. By showing the expected output in response to each input, they supplement the specs provided here.
5. Don't be afraid to [step through your code in the debugger](https://mediaspace.msu.edu/media/Merge_Sort+Recursive+Work+using+Debugger/1_h0i8pvg2): it will help you figure out where you're going wrong far more quickly than ad-hoc print statements!
6. Throughout the specs, we mention Python double-underscore "magic" methods. These are central to the structure of object-oriented programming in Python, and will continue to appear in future projects in CSE 331 and beyond. [This page](https://rszalski.github.io/magicmethods/) is a great reference if you'd like to learn more about how they work!
7. There are two functions which may seem a little odd to you *_find_nodes* and *_remove_node*. These functions are intended as helper functions to help you reuse code and allow you to practice writing modular code.
8. We **strongly** encourage you to avoid calling remove\_first in remove\_all. Why? It's far less efficient to repeatedly call remove\_first, as each call to remove\_first begins searching at the beginning of the list. In the worst case, this will lead our function to operate with O(n^2) time complexity, **violating the required time complexity.**
9. We **strongly** encourage you to implement reverse in-place, without creating any new Node objects and instead rearranging prev and next pointers. Why? It's far less efficient to rebuild the DLL than it is to simply adjust references, as it's far more work to construct a brand new Node object than it is to simply adjust an existing one's references.
10. In the testcases for this project, you will notice the use of assertEqual and assertIs. What's the difference? It ties back to the difference between == and is in Python. The double-equal sign compares *values* in Python, while the is operator compares *memory addresses* in Python. Put simply, the is keyword is stronger than ==: if two objects are at the same memory address, they must contain the same value. However, it is possible for two objects *not* at the same memory address to have the same value. In other words, if a is b then we know a == b as well, but if a == b we cannot conclude a is b. A great read on the subject is [available here](https://realpython.com/courses/python-is-identity-vs-equality/).

# Assignment Specifications

**class Node:**

*DO NOT MODIFY the following attributes/functions*

- **Attributes**
  - **value: T:** Value held by the Node. Note that this may be any type, such as a str, int, float, dict, or a more complex object.
  - **next: Node:** Reference to the next Node in the linked list (may be None).
  - **prev: Node:** Reference to the previous Node in the linked list (may be None).
  - **child: Node:** Reference to the child Node of this Node. Note: this will only be used for the application problem, you should not be using the **child** member in any of your functions aside from the application problem.
- **\_\_init\_\_(self, value: T, next: Node = None, prev: Node = None) -> None**
  - Constructs a doubly linked list node.
  - **value: T:** Value held by the Node.
  - **next: Node:** Reference to the next Node in the linked list (may be None).
  - **prev: Node:** Reference to the previous Node in the linked list (may be None).
  - **Returns:** None.
- **\_\_str\_\_(self) -> str** and **\_\_repr\_\_(self) -> str**
  - Represents the Node as a string.
  - Note that Python will automatically invoke this function when using printing a Node to the console, and PyCharm will automatically invoke this function when displaying a Node in the debugger.
  - As with all double-underscore "magic" methods in Python (see note 5), this function may be called with str(node) or repr(node). It is not necessary (and stylistically improper) to use node.\_\_str\_\_() or node.\_\_repr\_\_(), just as it is preferable to call len(some\_list) instead of some\_list.\_\_len\_\_().
  - **Returns:** str.

**class DLL:**

*DO NOT MODIFY the following attributes/functions*

- **Attributes**
  - **head: Node:** Head (first node) of the doubly linked list (may be None).
  - **tail: Node:** Tail (last node) of the doubly linked list (may be None).
  - **size: int:** Number of nodes in the doubly linked list.
  - Note that the implementation in this project does not use a [sentinel node](https://en.wikipedia.org/wiki/Sentinel_node). As such, an empty DLL will have head and tail attributes which are None.
- **\_\_init\_\_(self) -> None**
  - Construct an empty DLL. Initialize the head and tail to None, and set the size to zero.
  - **Returns:** None.
- **\_\_str\_\_(self) -> str** and **\_\_repr\_\_(self) -> str**
  - Represents the DLL as a string of the form "value <-> value <-> ... <-> value."
  - Note that Python will automatically invoke this function when printing a DLL to the console, and PyCharm will automatically invoke this function when displaying a DLL in the debugger.
  - As with all double-underscore "magic" methods in Python (see note 5), this function may be called with str(dll) or repr(dll). It is not necessary (and stylistically improper) to use dll.\_\_str\_\_() or dll.\_\_repr\_\_(), just as it is preferable to call len(some\_list) instead of some\_list.\_\_len\_\_().
  - **Returns:** str.

*IMPLEMENT the following functions*

- **empty(self) -> bool**
  - Returns a boolean indicating whether the DLL is empty.
  - *Required time complexity:* O(1).
  - *Required space complexity:* O(1).
  - **Returns:** True if DLL is empty, else False.
- **push(self, val: T, back: bool = True) -> None**
  - Adds a Node containing val to the back (or front) of the DLL and updates size accordingly.
  - *Required time complexity:* O(1).
  - *Required space complexity:* O(1).
  - **val: T:** Value to be added to the DLL.
  - **back: bool:** If True, add val to the back of the DLL. If False, add to the front. Note that the default value is True.
  - **Returns:** None.
- **pop(self, back: bool = True) -> None**
  - Removes a Node from the back (or front) of the DLL and updates size accordingly.
  - In the case that the DLL is empty, pop does nothing.
  - *Required time complexity:* O(1).
  - *Required space complexity:* O(1).
  - **back: bool:** If True, remove from the back of the DLL. If False, remove from the front. Note that the default value is True.
  - **Returns:** None.
- **list\_to\_dll(self, source: list[T]) -> None**
  - Creates a DLL from a standard Python list.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(n).
  - **source: list[T]:** Standard Python list from which to construct DLL.
  - **Returns:** None.
- **dll\_to\_list(self) -> list[T]**
  - Creates a standard Python list from a DLL.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(n).
  - **Returns:** list[T] containing the values of the nodes in the DLL.
- **def \_find\_nodes(self, val: T, find\_first: bool =False) -> List[Node]:**
  - Construct list of Node with value val in the DLL and returns the associated Node object list
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(1).
  - MUST BE CALLED FROM find AND find\_all
    - If find and find\_all do not call \_find\_nodes, **all testcase and manual points** for find and find\_all will be forfeited.
  - Will not be tested explicitly
    - Tests for find and find\_all will ensure functionality
  - **val: T:** Value to be found in the DLL.
  - **find\_first: bool:**  if True find only the first element in the DLL, it false find all instances of the elements in the DLL.
  - **Returns:** list of Node objects in the DLL whose value is val. If val does not exist in the DLL, returns empty list.
- **find(self, val: T) -> Node**
  - Finds first Node with value val in the DLL and returns the associated Node object.
  - *Requires call to* \_find\_nodes
    - Failure to call \_find\_nodes will result in **all testcase and manual points** being forfeited for find.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(1).
  - **val: T:** Value to be found in the DLL.
  - **Returns:** first Node object in the DLL whose value is val. If val does not exist in the DLL, returns an empty list.
- **find\_all(self, val: T) -> list[Node]**
  - Finds all Node objects with value val in the DLL and returns a standard Python list of the associated Node objects.
  - *Requires call to* \_find\_nodes
    - Failure to call \_find\_nodes will result in **all testcase and manual points** being forfeited for find\_all.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(n).
  - **val: T:** Value to be found in the DLL.
  - **Returns:** standard Python list of all Node objects in the DLL whose value is val. If val does not exist in the DLL, returns an empty list.
- **\_remove\_node(self, to\_remove: Node) -> None**
  - Given a reference to a node in the linked list, remove it
  - MUST BE CALLED FROM remove\_first  AND remove\_all
  - Will not be tested explicitly
    - Tests for remove\_first and remove\_all will ensure functionality
  - *Required time complexity:* O(1).
  - *Required space complexity:* O(1).
  - **to\_remove: Node:** Node to be removed from the DLL.
  - **Returns:** None.
- **remove(self, val: T) -> bool**
  - removes first Node with value val in the DLL.
  - MUST CALL \_remove\_node
    - Failure to call \remove\_node will result in **all testcase and manual points** being forfeited for remove.
  - Hint
    - Use of `find` allows this to be implemented in less than 10 lines.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(1).
  - **val: T:** Value to be removed from the DLL.
  - **Returns:** True if a Node with value val was found and removed from the DLL, else False.
- **remove\_all(self, val: T) -> int**
  - removes all Node objects with value val in the DLL. See note 7.
  - MUST CALL \_remove\_node
    - Failure to call \remove\_node will result in **all testcase and manual points** being forfeited for remove\_all.
  - Hint
    - Use of `find_all` allows this to be implemented in less than 10 lines.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(n).
  - **val: T:** Value to be removed from the DLL.
  - **Returns:** number of Node objects with value val removed from the DLL. If no node containing val exists in the DLL, returns 0.
- **reverse(self) -> None**
  - Reverses the DLL in-place by modifying all next and prev references of Node objects in DLL. Updates self.head and self.tail accordingly. See note 7.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(1).
  - **Returns:** None.

# Application Problem: Secretary Scheduler

You work as a secretary at ONSAYINGS™, a company dedicated entirely to developing captions for those fire Instagram pictures 🔥. Your daily routine is composed of rearranging your bosses multilevel DLL schedule into a single level DLL that follows the chronological order of tasks.

Each node in the multilevel DLL has an extra data member named child. Everything in the child’s DLL should occur after the current `node` but before current `node.next`. 

A small aside:
Though a multi-level structure seems odd, there are actually applications of this structure in the popular Pandas data science library. The Pandas library supports a multi-index structure that is structured in this way. If you would like to learn more, check out the links [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html) and [here](https://datascientyst.com/flatten-multiindex-in-pandas/).

**Multi-level Input**

![](img/Multilevel_DLL.png)


**Single-level Output**

![](img/Single_level_DLL.png)

**Explanation**
- A is the first node in multi so it will also be first in single level
- A has no children so B is A's next
- B has children so those are brought up to be B's next
- J has no children so it's next would be B's next, C
- C has a child so E becomes C's next
- E has no child so E's next stays the same, F
- F has a child so it's next becomes F's Next
- H has no next and no child so H's next is F's next
- G's has no next and no child so it's next is D
- Compiling this gives you the single level DLL above


After a few weeks on the job, you realize you can put your use 331 skills to work to build an algorithm called `secretary_scheduler` to transform a multilevel DLL to a single level DLL. This will give you more time to focus on what really matters! Speed running 3 stars on Angry Birds! 


Let's summarize:

- **secretary\_scheduler (dll: DLL) -> DLL**
  - Turns a multilevel dll into a single level dll
  - Child nodes are placed after the `parent` node but before the `parent.next` node in the final DLL.
  - *Required time complexity:* O(n).
  - *Required space complexity:* O(n).
  - **dll: DLL:** A DLL where each Node holds a value of str where the string is the task. The Node also holds a child in `.child` and stores the child DLL to the current node.
  - **Returns:** a DLL holding str representing the names of all of the tasks
  - Notes:
    - If the DLL is empty, return an empty DLL.
    - When `node.child` is `None` it means there is no child DLL
    - All child values should be `None` in the DLL that is returned
    

**Example 1**

```
Input
A - B - C - D
    |   |
    E   F
    

Output
A - B - E - C - F - D
```

- **Explanation:**
  - A is the first node in the input  so it is the first in the output
  - A has no children so it is followed by its next, B.
  - B has a child DLL so nodes from that are inserted next, E.
  - All of B’s child’s are finished so it goes to B’s next, C
  - C has a child DLL so nodes from that are inserted next, F.
  - All of C’s child’s are finished so it goes to C’s next, D
  - Compiling the nodes into a DLL gives us the desired result.

**Example 2**
```
Input
A - B - C
|       | 
E - F   G
        |
        H
Output
A - E - F - B - G - H
```

- **Explanation:**
  - A is the first node in the input so it is the first in the output
  - A has 2 children so they will be placed before B
  - E is first in A’s child DLL so it is placed first
  - E has no children so its next is placed into the output, F
  - F is the last element in the child DLL and has no children so A’s Next is placed in the output, B
  - B has no child DLL so it's next is C
  - C has child DLL with start of G so G is placed in output
  - G has child DLL beginning with H so H is placed in output
  - Compiling the nodes into a DLL gives us the desired result.

**Example 3**
```
Input
A - B - C
    |
    D - F
    |   |
    E   H
    |
    G

Output 
A - B - D - E - G - F - H - C
```

- **Explanation:**
  - A is the first node in the input  so it is the first in the output
  - A has no children so it is followed by its next, B.
  - B has a child DLL so nodes from that are inserted next, D.
  - D has a child DLL so that is inserted next, E
  - E has child DLL so that is inserted next, G
  - G has no children and no next so the next element inserted is F
  - F has child DLL so that is inserted next, H
  - H has no child DLL and no next so F’s next is inserted, C
  - C has no DLL and no next so we are finished
  - Compiling the nodes into a DLL gives us the desired result.

# Submission

Be sure to upload the following deliverables in a .zip folder to Mimir by 10:00p ET on Thursday, February 10th.

    Project03.zip
        |— Project03/
            |— feedback.xml   (for project feedback)
            |— __init__.py    (for proper Mimir testcase loading)
            |— solution.py    (contains your solution source code)

Starter code and local test cases can be found here on Mimir by clicking the "Download Starter Code" button, or on D2L.
* See tutorial video on [how to download your starter code from D2L and open it in PyCharm](https://youtu.be/LMNtMxPLJMA)

# Grading

- Tests (70)
  - Point distribution is specified in testcases
- Manual (30)
  - Time and space complexity points are **all-or-nothing** for each function. If you fail to meet time **or** space complexity in a given function, you do not receive manual points for that function.
  - Using a Python's list to solve the DLL's application problem is -5pts
  - empty: \_\_ / 1
  - push: \_\_ / 2
  - pop: \_\_ / 2
  - list\_to\_dll: \_\_ / 2
  - dll\_to\_list: \_\_ / 2
  - \_find\_nodes: \_/2
    - If find and find\_all do not call \_find\_nodes, **all testcase and manual points** for find and find\_all  will be forfeited.
    - If \_find\_nodes violates time and/or space complexity and is called by find and find\_all  (as it must be), **all manual points** will be forfeited for the three functions
  - find: \_\_ / 2
  - find\_all: \_\_ / 2
  - \_remove\_node: \_\_ / 2
    - If remove\_first  and remove\_all do not call \_remove\_node, **all testcase and manual points** for remove\_first  and remove\_all will be forfeited.
    - If \_remove\_node violates time and/or space complexity and is called by remove\_first  and remove\_all (as it must be), **all manual points** will be forfeited for the three functions.
  - remove: \_\_ / 2
  - remove\_all: \_\_ / 2
  - reverse: \_\_ / 2
  - secretary\_scheduler: \_\_ / 7

# Authors

Project Updated by: Matt Kight & Lukas Richters
Original authors: Andrew McDonald, Alex Woodring & Andrew Haas




