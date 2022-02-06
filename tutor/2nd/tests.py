import unittest
from solution import RecursiveSinglyLinkedList as SLL, SLLNode, reverse_playlist
import random


class MyTestCase(unittest.TestCase):

    def test_to_string(self):

        sll = SLL()

        # 1. Get the string of an empty list
        self.assertEqual("None", sll.to_string(sll.head))  # 1

        # 2. Get the string of an one element list
        sll.head = SLLNode(3)
        self.assertEqual("3", sll.to_string(sll.head))  # 2

        # 3. Get the string of a two element list
        sll.head.next = SLLNode(3)
        self.assertEqual("3 --> 3", sll.to_string(sll.head))  # 3

        # 4. Get the string of a multi-element list
        sll.head.next.next = SLLNode(1)
        self.assertEqual("3 --> 3 --> 1", sll.to_string(sll.head))  # 4

        # 5. Type Agnostic test
        sll = SLL()
        sll.head = SLLNode('Hello')
        sll.head.next = SLLNode('World!')
        self.assertEqual("Hello --> World!", sll.to_string(sll.head))  # 5

    def test_length(self):

        sll = SLL()

        # 1. Get the length of an empty list
        self.assertEqual(0, sll.length(sll.head))  # 1

        # 2. Get the length of a list with only one element
        sll.head = SLLNode(2)
        self.assertEqual(1, sll.length(sll.head))  # 2

        # 3. Get the length of a list with two elements
        sll.head.next = SLLNode(5)
        self.assertEqual(2, sll.length(sll.head))  # 3

        # 4. Get the length of a list with multiple elements
        sll.head.next.next = SLLNode(0)
        sll.head.next.next.next = SLLNode(0)
        self.assertEqual(4, sll.length(sll.head))  # 4

        # 5. Type Agnostic test
        sll = SLL()
        sll.head = SLLNode('Hello')
        sll.head.next = SLLNode('World!')
        self.assertEqual(2, sll.length(sll.head))  # 5

    def test_sum_list(self):

        sll = SLL()

        # 1. Get the sum of an empty list
        self.assertIs(None, sll.sum_list(sll.head))  # 1

        # 2. Get the sum of a list with one SLLNode
        sll.head = SLLNode(3)
        self.assertEqual(3, sll.sum_list(sll.head))  # 2

        # 3. Get the sum of a list with two SLLNodes
        sll.head.next = SLLNode(5)
        self.assertEqual(8, sll.sum_list(sll.head))  # 3

        # 4. Get the sum of a list with multiple SLLNodes
        sll.head.next.next = SLLNode(0)
        sll.head.next.next.next = SLLNode(1)
        self.assertEqual(9, sll.sum_list(sll.head))  # 4

        # 5. Type Agnostic test
        sll = SLL()
        sll.head = SLLNode('Hello')
        sll.head.next = SLLNode('World!')
        sll.head.next.next = SLLNode('ThereShouldBeNoSpaces')
        self.assertEqual('HelloWorld!ThereShouldBeNoSpaces', sll.sum_list(sll.head))  # 5

    def test_search(self):

        sll = SLL()

        # 1. Try to search an empty List
        self.assertEqual(False, sll.search(331))  # 1

        sll.head = SLLNode(4)
        sll.head.next = SLLNode(2)
        sll.head.next.next = SLLNode(0)

        # 2. Search for a SLLNode at the start of the list
        self.assertEqual(True, sll.search(4))  # 2

        # 3. Search for a value that doesn't exist in the list
        self.assertEqual(False, sll.search(3))  # 3

        # 4. Search for a SLLNode in the middle of the list
        self.assertEqual(True, sll.search(2))  # 4

        # 5. Search for a SLLNode at the end of the list
        self.assertEqual(True, sll.search(0))  # 5

        # 6. Type Agnostic test
        sll = SLL()
        sll.head = SLLNode('Hello')
        sll.head.next = SLLNode('World!')
        sll.head.next.next = SLLNode('ThereShouldBeNoSpaces')
        self.assertEqual(True, sll.search('World!'))  # 6

    def test_count(self):

        sll = SLL()

        # 1. Try to get a count from an empty list
        self.assertEqual(0, sll.count(7))  # 1

        # 2. Get the number of 2's in the one element list
        sll.head = SLLNode(3)
        self.assertEqual(1, sll.count(3))  # 2

        # 3. Get the number of 5's in the two element list
        sll.head.next = SLLNode(5)
        self.assertEqual(1, sll.count(5))  # 3

        # 4. Get the number of 0's from tha multi-element list
        sll.head.next.next = SLLNode(0)
        sll.head.next.next.next = SLLNode(0)
        self.assertEqual(2, sll.count(0))  # 4

        # 5. Try to get the count of a number that doesn't exist in the list
        self.assertEqual(0, sll.count(42))  # 5

        # 6. Type Agnostic test
        sll = SLL()
        sll.head = SLLNode('Hello')
        sll.head.next = SLLNode('World!')
        sll.head.next.next = SLLNode('Hello')
        self.assertEqual(2, sll.count('Hello'))  # 6

    def test_push(self):

        sll = SLL()

        # 1. Insert into an empty list
        sll.push(3)
        self.assertEqual(3, sll.head.val)  # 1
        self.assertEqual(3, sll.tail.val)  # 1

        # 2. Insert into a one element list
        sll.push(3)
        self.assertEqual(3, sll.head.next.val)  # 2
        self.assertEqual(3, sll.tail.val)  # 1

        # 3. Push into a list with multiple SLLNodes
        sll.push(1)
        self.assertEqual(1, sll.head.next.next.val)  # 3
        self.assertEqual(1, sll.tail.val)  # 1
        self.assertEqual(None, sll.head.next.next.next)  # 3

        # 4. Front test
        sll.push(4, False)
        self.assertEqual(4, sll.head.val)  # 4
        self.assertEqual(3, sll.head.next.val)  # 4
        self.assertEqual(3, sll.head.next.next.val)  # 4
        self.assertEqual(1, sll.head.next.next.next.val)  # 4
        self.assertEqual(1, sll.tail.val)  # 4
        self.assertEqual(None, sll.head.next.next.next.next)  # 4

        # 5. Type Agnostic test
        sll = SLL()
        sll.push('CSE331')
        self.assertEqual('CSE331', sll.head.val)  # 5
        self.assertEqual('CSE331', sll.tail.val)  # 5

        # 6. Type Agnostic test 2
        sll.push('CSE498')
        self.assertEqual('CSE331', sll.head.val)  # 6
        self.assertEqual('CSE498', sll.head.next.val)  # 6
        self.assertEqual('CSE498', sll.tail.val)  # 6

    def test_remove(self):

        sll = SLL()

        # 1. Removing from an empty list
        self.assertEqual(False, sll.remove(42))  # 1
        self.assertEqual(None, sll.head)  # 1
        self.assertEqual(None, sll.tail)  # 1

        sll.head = SLLNode(3)
        sll.head.next = SLLNode(4)
        sll.head.next.next = SLLNode(3)
        sll.head.next.next.next = SLLNode(1)
        sll.tail = sll.head.next.next.next

        # 2. Remove from the middle of the list
        self.assertEqual(True, sll.remove(4))  # 2
        self.assertEqual(3, sll.head.val)  # 2
        self.assertEqual(3, sll.head.next.val)  # 2
        self.assertEqual(1, sll.head.next.next.val)  # 2
        self.assertEqual(None, sll.head.next.next.next)  # 2
        self.assertEqual(1, sll.tail.val)  # 2

        # 3. Remove from the end of the list
        self.assertEqual(True, sll.remove(1))  # 3
        self.assertEqual(3, sll.head.val)  # 3
        self.assertEqual(3, sll.head.next.val)  # 3
        self.assertEqual(None, sll.head.next.next)  # 3
        self.assertEqual(3, sll.tail.val)  # 3

        # 4. Remove from the front of the list
        self.assertEqual(True, sll.remove(3))  # 4
        self.assertEqual(3, sll.head.val)  # 4
        self.assertEqual(None, sll.head.next)  # 4
        self.assertEqual(3, sll.tail.val)  # 4

        # 5. Remove the last SLLNode in the list
        self.assertEqual(True, sll.remove(3))  # 5
        print("Ho\n", sll.tail)
        self.assertEqual(None, sll.head)  # 5
        self.assertEqual(None, sll.tail)  # 5

    def test_remove_all(self):

        sll = SLL()
        sll.head = SLLNode(2)
        sll.head.next = SLLNode(3)
        sll.head.next.next = SLLNode(3)
        sll.head.next.next.next = SLLNode(1)
        sll.head.next.next.next.next = SLLNode(4)
        sll.head.next.next.next.next.next = SLLNode(4)
        sll.head.next.next.next.next.next.next = SLLNode(1)

        # 1. Try to remove an element that doesn't exist in the list
        self.assertEqual(False, sll.remove_all(6))  # 1
        self.assertEqual(2, sll.head.val)  # 1
        self.assertEqual(3, sll.head.next.val)  # 1
        self.assertEqual(3, sll.head.next.next.val)  # 1
        self.assertEqual(1, sll.head.next.next.next.val)  # 1
        self.assertEqual(4, sll.head.next.next.next.next.val)  # 1
        self.assertEqual(4, sll.head.next.next.next.next.next.val)  # 1
        self.assertEqual(1, sll.head.next.next.next.next.next.next.val)  # 1
        self.assertEqual(None, sll.head.next.next.next.next.next.next.next)  # 1

        # 2. Try to remove only the head
        self.assertEqual(True, sll.remove_all(2))  # 2
        self.assertEqual(3, sll.head.val)  # 2
        self.assertEqual(3, sll.head.next.val)  # 2
        self.assertEqual(1, sll.head.next.next.val)  # 2
        self.assertEqual(4, sll.head.next.next.next.val)  # 2
        self.assertEqual(4, sll.head.next.next.next.next.val)  # 2
        self.assertEqual(1, sll.head.next.next.next.next.next.val)  # 2
        self.assertEqual(None, sll.head.next.next.next.next.next.next)  # 2

        # 3. Remove multiple 3's from the start of the list
        self.assertEqual(True, sll.remove_all(3))  # 3
        self.assertEqual(1, sll.head.val)  # 3
        self.assertEqual(4, sll.head.next.val)  # 3
        self.assertEqual(4, sll.head.next.next.val)  # 3
        self.assertEqual(1, sll.head.next.next.next.val)  # 3
        self.assertEqual(None, sll.head.next.next.next.next)  # 3

        # 4. remove elements from the middle of the list
        self.assertEqual(True, sll.remove_all(4))  # 4
        self.assertEqual(1, sll.head.val)  # 4
        self.assertEqual(1, sll.head.next.val)  # 4
        self.assertEqual(None, sll.head.next.next)  # 4

        temp = sll.head.next
        sll.head.next = SLLNode(10)
        sll.head.next.next = temp

        # 5. remove elements from the middle and end of the list
        self.assertEqual(True, sll.remove_all(1))  # 5
        self.assertEqual(10, sll.head.val)  # 5
        self.assertEqual(None, sll.head.next)  # 5

        # 6. remove the only element of the list
        self.assertEqual(True, sll.remove_all(10))  # 6
        self.assertEqual(None, sll.head)  # 6

        # 7. Try to remove from an empty list
        self.assertEqual(False, sll.remove_all(2))  # 7
        self.assertEqual(None, sll.head)  # 7

    def test_comprehensive(self):

        def sll_to_list(sll):
            """
              This function is only used in the comprehensive test. It will take in a singly link list
              and create a python list with the same contents
              :param sll: Source singly linked list
              :return: A python list the same contents and order as the given singly linked list
              """

            new_list = []

            def walk_sll(curr):
                if curr is None:
                    return
                new_list.append(curr.val)
                walk_sll(curr.next)

            walk_sll(sll.head)
            return new_list

        random.seed(331)
        sol = list(range(200)) + list(range(50))  # we want some duplicates to see how those are handled
        subject = SLL()
        random.shuffle(sol)
        for i, val in enumerate(sol):
            subject.push(val)  # Check if push is correct
            self.assertEqual(sol[:i + 1], sll_to_list(subject))

        input_string = ""
        for i in range(len(sol)):
            input_string += str(sol[i])
            if i != len(sol) - 1:
                input_string += " --> "
        self.assertEqual(input_string, subject.to_string(subject.head))  # check if to_string is correct

        self.assertEqual(len(sol), subject.length(subject.head))  # check if the length is correct

        self.assertEqual(sum(sol), subject.sum_list(subject.head))  # check if sum_list is correct

        for val in sol:
            # make sure count is correct
            self.assertEqual(sol.count(val), subject.count(val))
            if sol.count(val) > 0:
                # make sure search is correct when the val is in the list
                self.assertTrue(subject.search(val))
            else:
                # make sure search is correct when the val isn't in the list
                self.assertFalse(subject.search(val))

            subject.remove(val)

            if val in sol:
                sol.remove(val)

            self.assertEqual(sol, sll_to_list(subject))  # make sure remove is working correctly

            if val < 50:
                # make sure remove all is working correctly
                subject.remove_all(val)

                for count in range(sol.count(val)):
                    sol.remove(val)

    def test_reverse_playlist(self):

        sll = SLL()

        # 1. Try to reverse an empty playlist
        reverse_playlist(sll, sll.head)
        self.assertEqual(None, sll.head)  # 1
        self.assertEqual(None, sll.tail)  # 1

        # 2. Reverse a one element playlist
        sll.head = SLLNode('Fruit Salad')
        sll.tail = sll.head
        reverse_playlist(sll, sll.head)
        self.assertEqual('Fruit Salad', sll.head.val)  # 2
        self.assertEqual(None, sll.head.next)  # 2
        self.assertEqual('Fruit Salad', sll.tail.val)  # 2

        # 3. Reverse a two element playlist
        sll = SLL()
        sll.head = SLLNode('Fruit Salad')
        sll.head.next = SLLNode('Hot Potato')
        sll.tail = sll.head.next
        reverse_playlist(sll, sll.head)
        self.assertEqual('Hot Potato', sll.head.val)  # 3
        self.assertEqual('Fruit Salad', sll.head.next.val)  # 3
        self.assertEqual(None, sll.head.next.next)  # 3
        self.assertEqual('Fruit Salad', sll.tail.val)  # 3

        # 4. Reverse a three element playlist
        sll.head = SLLNode('Were All In This Together')
        sll.head.next = SLLNode('Start of Something New')
        sll.head.next.next = SLLNode('Breaking Free')
        sll.tail = sll.head.next.next
        reverse_playlist(sll, sll.head)
        self.assertEqual('Breaking Free', sll.head.val)  # 4
        self.assertEqual('Start of Something New', sll.head.next.val)  # 4
        self.assertEqual('Were All In This Together', sll.head.next.next.val)  # 4
        self.assertEqual(None, sll.head.next.next.next)  # 4
        self.assertEqual('Were All In This Together', sll.tail.val)  # 4

        # 5. Reverse a multi-element playlist
        sll = SLL()
        sll.head = SLLNode('City is Ours')
        sll.head.next = SLLNode('Big Time Rush')
        sll.head.next.next = SLLNode('Halfway There')
        sll.head.next.next.next = SLLNode('Famous')
        sll.tail = sll.head.next.next.next
        reverse_playlist(sll, sll.head)
        self.assertEqual('Famous', sll.head.val)  # 5
        self.assertEqual('Halfway There', sll.head.next.val)  # 5
        self.assertEqual('Big Time Rush', sll.head.next.next.val)  # 5
        self.assertEqual('City is Ours', sll.head.next.next.next.val)  # 5
        self.assertEqual(None, sll.head.next.next.next.next)  # 5
        self.assertEqual('City is Ours', sll.tail.val)  # 5

        # 6. Reverse a long playlist
        sll = SLL()
        sll.head = SLLNode('Famous')
        sll.head.next = SLLNode('Big Time Rush')
        sll.head.next.next = SLLNode('City is Ours')
        sll.head.next.next.next = SLLNode('CSE331: The Theme Song')
        sll.head.next.next.next.next = SLLNode('Hot Potato')
        sll.head.next.next.next.next.next = SLLNode('Fruit Salad')
        sll.head.next.next.next.next.next.next = SLLNode('Breaking Free')
        sll.head.next.next.next.next.next.next.next = SLLNode('Start of Something New')
        sll.head.next.next.next.next.next.next.next.next = SLLNode('Found a Way')
        sll.head.next.next.next.next.next.next.next.next.next = SLLNode('Ill be There for You')
        sll.tail = sll.head.next.next.next.next.next.next.next.next.next
        reverse_playlist(sll, sll.head)
        self.assertEqual('Ill be There for You', sll.head.val)  # 6
        self.assertEqual('Found a Way', sll.head.next.val)  # 6
        self.assertEqual('Start of Something New', sll.head.next.next.val)  # 6
        self.assertEqual('Breaking Free', sll.head.next.next.next.val)  # 6
        self.assertEqual('Fruit Salad', sll.head.next.next.next.next.val)  # 6
        self.assertEqual('Hot Potato', sll.head.next.next.next.next.next.val)  # 6
        self.assertEqual('CSE331: The Theme Song', sll.head.next.next.next.next.next.next.val)  # 6
        self.assertEqual('City is Ours', sll.head.next.next.next.next.next.next.next.val)  # 6
        self.assertEqual('Big Time Rush', sll.head.next.next.next.next.next.next.next.next.val)  # 6
        self.assertEqual('Famous', sll.head.next.next.next.next.next.next.next.next.next.val)  # 6
        self.assertEqual(None, sll.head.next.next.next.next.next.next.next.next.next.next)  # 6
        self.assertEqual('Famous', sll.tail.val)  # 6


if __name__ == '__main__':
    unittest.main()
