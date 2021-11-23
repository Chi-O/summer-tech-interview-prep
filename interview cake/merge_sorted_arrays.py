import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list

    l1 = my_list
    l2 = alices_list

    m = len(my_list) 
    n = len(alices_list)

    res = [0] * (m + n)

    p1 = 0
    p2 = 0
    i = 0

    while i < (m + n):
        # check if lists are exhausted
        l1_exhausted = p1 >= m
        l2_exhausted = p2 >= n

        # add from l1 if
        if not l1_exhausted and (l2_exhausted or l1[p1] < l2[p2]):
            res[i] = l1[p1]
            p1 += 1
        else:
            res[i] = l2[p2]
            p2 += 1

        i += 1
        
    return res


















# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)