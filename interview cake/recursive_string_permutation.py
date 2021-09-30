"""
Write a recursive function for generating all permutations of an input string. Return them as a set.
Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.

To start, assume every character in the input string is unique.

Your function can have loops—it just needs to also be recursive.
"""

# APPROACH:
# 1) recursively remove last char of string
#    base case: only one char in substring (len(substring) <= 1)
# 2) find all permutations of substring
# 3) up the recursive stack:
#       for each permution:
        #     for each position in permutation:
        #         place last char in perm

        #         add perm to set
        
        # return perm set

def get_permutations(msg):
    # base case: only one char (only one permutation)
    if len(msg) <=  1:
        return set([msg])

    # remove last char (recursively)
    except_last_char = msg[:-1]
    last_char = msg[-1]

    perms_of_except_last_char = get_permutations(except_last_char)

    # place char at each position, for each permutation
    perms = set()

    for perm in perms_of_except_last_char:
        for pos in range(len(except_last_char) + 1):
            this_perm = ( perm[:pos] + last_char + perm[pos:] )

            perms.add(this_perm)
        
    return perms

print(get_permutations("abbdd"))