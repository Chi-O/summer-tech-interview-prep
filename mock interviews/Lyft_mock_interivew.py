# Given a list, return a reversed version of the list.
# """
# traverse the list from last to first element, and copy to a new list
# """

# def reverse_list(arr):
#     # make a copy
#     new = []
#     # traverse the list from the last element to first
#     for i in range(len(arr) - 1, -1, -1):
#         new.append(arr[i])
    
#     return new

# arr = [5, 6, 3, 2] 
# # 2, 3, 6, 5

# print(reverse_list(arr))


"""
Reverse a string without affecting special characters
Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’),
reverse the string in a way that special characters are not affected.
Example:
Input: 'a$$$b^^^c***'
Output: 'c$$$b^^^a***'

[a, b, c]
copy = []
"""

"""
traverse the input string
check that its an alphabet
store alphabets in alph_array
create an empty copy
populating the copy:
    if alphabet:
        insert last element from alpha_array
    else:
        copy the orignal character from input string

65-90, 97-122
"""


# ====================
# Running testcase for a$$$b^^^c***
# FAILED: ['c', '$', '$', '$', 'b', '^', '^', '^', 'c', '*', '*', '*'] does not match c$$$b^^^a***
# ====================
# Running testcase for abc&&&def
# FAILED: ['f', 'e', 'd', '&', '&', '&', 'd', 'e', 'f'] does not match fed&&&cba


def special_reverse(input_str):
    # TODO: Your solution
    alpha_arr = []
    copy = []
    
    for ch in input_str:
        if (65 <= ord(ch) and 90 >= ord(ch)) or (97 <= ord(ch) and 122 >= ord(ch)):
            alpha_arr.append(ch)
        else:
            continue
    
    # for ch in input_str:
    #     if ch in alpha_arr:
    #         copy.append(alpha_arr.pop())
    #     else:
    #         copy.append(ch)
    
    print(alpha_arr)
    
    for ch in input_str:
        if ch in alpha_arr:
             alpha_arr.pop()

    
    print(alpha_arr)
    
    # return str(copy)
    return 


class TestCase:
    def __init__(self, input_str, answer):
        self.input_str = input_str
        self.answer = answer

    def run_test(self):
        print("=" * 20)
        print(f"Running testcase for {self.input_str}")
        try:
            output_str = special_reverse(self.input_str)
            assert output_str == self.answer
            print("PASSED")
        except AssertionError:
            print(f"FAILED: {output_str} does not match {self.answer}")


TESTCASES = [
    TestCase("a$$$b^^^c***", "c$$$b^^^a***"),
    TestCase("abc&&&def", "fed&&&cba"),
]

# for testcase in TESTCASES:
#     testcase.run_test()

special_reverse("a$$$b^^^c***")