import unittest
from solution import SinglyLinkedList as SLL, SLLNode, max_crash_dist
import random


class MyTestCase(unittest.TestCase):

    def sll_to_list(self, sll):
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

    def test_to_string(self):

        sll = SLL()
        # 1. Get the string of an empty list
        self.assertEqual("None", sll.to_string())  # 1

        # 2. Get the string of an one element list
        sll.head = SLLNode(3)
        self.assertEqual("3", sll.to_string())  # 2

        # 3. Get the string of a two element list
        sll.head.next = SLLNode(3)
        self.assertEqual("3 --> 3", sll.to_string())  # 3

        # 4. Get the string of a multi-element list
        sll.head.next.next = SLLNode(1)
        self.assertEqual("3 --> 3 --> 1", sll.to_string())  # 4

    def test_length(self):

        sll = SLL()
        # 1. Get the length of an empty list
        self.assertEqual(0, sll.length())  # 1

        # 2. Get the length of a list with only one element
        sll.head = SLLNode(2)
        self.assertEqual(1, sll.length())  # 2

        # 3. Get the length of a list with two elements
        sll.head.next = SLLNode(5)
        self.assertEqual(2, sll.length())  # 3

        # 4. Get the length of a list with multiple elements
        sll.head.next.next = SLLNode(0)
        sll.head.next.next.next = SLLNode(0)
        self.assertEqual(4, sll.length())  # 4

    def test_sum_list(self):

        sll = SLL()

        # 1. Get the sum of an empty list
        self.assertIs(None, sll.sum_list())  # 1

        # 2. Get the sum of a list with one SLLNode
        sll.head = SLLNode(3)
        self.assertEqual(3, sll.sum_list())  # 2

        # 3. Get the sum of a list with two SLLNodes
        sll.head.next = SLLNode(5)
        self.assertEqual(8, sll.sum_list())  # 3

        # 4. Get the sum of a list with multiple SLLNodes
        sll.head.next.next = SLLNode(0)
        sll.head.next.next.next = SLLNode(1)
        self.assertEqual(9, sll.sum_list())  # 4

    def test_push(self):

        sll = SLL()
        # 1. Insert into an empty list
        sll.push(3)
        self.assertEqual(3, sll.head.val)  # 1

        # 2. Insert into a one element list
        sll.push(3)
        self.assertEqual(3, sll.head.next.val)  # 2

        # 3. Push into a list with multiple SLLNodes
        sll.push(1)
        self.assertEqual(1, sll.head.next.next.val)  # 3
        self.assertEqual(None, sll.head.next.next.next)  # 3

    def test_remove(self):

        sll = SLL()

        # 1. Removing from an empty list
        self.assertEqual(False, sll.remove(42))  # 1
        self.assertEqual(None, sll.head)  # 1

        sll.head = SLLNode(3)
        sll.head.next = SLLNode(4)
        sll.head.next.next = SLLNode(3)
        sll.head.next.next.next = SLLNode(1)

        # 2. Remove from the middle of the list
        self.assertEqual(True, sll.remove(4))  # 2
        self.assertEqual(3, sll.head.val)  # 2
        self.assertEqual(3, sll.head.next.val)  # 2
        self.assertEqual(1, sll.head.next.next.val)  # 2
        self.assertEqual(None, sll.head.next.next.next)  # 2

        # 3. Remove from the end of the list
        self.assertEqual(True, sll.remove(1))  # 3
        self.assertEqual(3, sll.head.val)  # 3
        self.assertEqual(3, sll.head.next.val)  # 3
        self.assertEqual(None, sll.head.next.next)  # 3

        # 4. Remove from the front of the list
        self.assertEqual(True, sll.remove(3))  # 4
        self.assertEqual(3, sll.head.val)  # 4
        self.assertEqual(None, sll.head.next)  # 4

        # 5. Remove the last SLLNode in the list
        self.assertEqual(True, sll.remove(3))  # 5
        self.assertEqual(None, sll.head)  # 5

    def test_remove_all(self):

        sll = SLL()
        sll.head = SLLNode(3)
        sll.head.next = SLLNode(3)
        sll.head.next.next = SLLNode(1)

        # 1. Try to remove an element that doesn't exist in the list
        self.assertEqual(False, sll.remove_all(6))  # 1
        self.assertEqual(3, sll.head.val)  # 1
        self.assertEqual(3, sll.head.next.val)  # 1
        self.assertEqual(1, sll.head.next.next.val)  # 1
        self.assertEqual(None, sll.head.next.next.next)  # 1

        # 2. Remove all of the 3's from the list
        self.assertEqual(True, sll.remove_all(3))  # 2
        self.assertEqual(1, sll.head.val)  # 2
        self.assertEqual(None, sll.head.next)  # 2

        # 3. Remove the last element from the list
        self.assertEqual(True, sll.remove_all(1))  # 3
        self.assertEqual(None, sll.head)  # 3

        # 4. Try to remove from an empty list
        self.assertEqual(False, sll.remove_all(2))  # 4
        self.assertEqual(None, sll.head)  # 4

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
        self.assertEqual(input_string, subject.to_string())  # check if to_string is correct

        self.assertEqual(len(sol), subject.length())  # check if the length is correct

        self.assertEqual(sum(sol), subject.sum_list())  # check if sum_list is correct

        for val in sol:
            # make sure count is correct
            self.assertEqual(sol.count(val), subject.count(val))
            if sol.count(val) > 0:
                # make sure search is correct when the val is in the lisr
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

    def test_max_crash_dist(self):

        ll = SLL()

        # 1: Empty SLL
        self.assertEqual(0, max_crash_dist(ll))  # 1

        # 2: One element SLL
        ll.push(1)
        self.assertEqual(0, max_crash_dist(ll))  # 2

        # 3: Longer SLL, only 1 perfect square
        ll.push(2)
        ll.push(3)
        self.assertEqual(0, max_crash_dist(ll))  # 3

        # 4: two perfect squares
        ll.push(4)
        self.assertEqual(3, max_crash_dist(ll))  # 4

        # 5: three perfect squares
        ll.push(9)
        self.assertEqual(3, max_crash_dist(ll))  # 5

        # 6: Longer test 1
        ll2 = SLL()
        for i in [2, 3, 5, 4, 6, 7, 9, 16, 22, 23, 24, 26, 27, 28, 25]:
            ll2.push(i)
        self.assertEqual(7, max_crash_dist(ll2))  # 6

        # 7: Longer test 2
        ll3 = SLL()
        for i in range(82):
            ll3.push(i)
        self.assertEqual(17, max_crash_dist(ll3))  # 7

        # 8. Long Test with no perfect squares
        ll4 = SLL()
        for i in range(145, 169):
            ll4.push(i)
        self.assertEqual(0, max_crash_dist(ll4))  # 8


if __name__ == '__main__':
    unittest.main()