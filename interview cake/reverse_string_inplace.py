def reverse_inplace(msg):
    left_index = 0
    right_index = len(msg) - 1

    # while they don't meet (middle char will be left untouched)
    while left_index < right_index:
        # swap characters
        msg[left_index], msg[right_index] = msg[right_index], msg[left_index]

        # move towards the middle
        left_index += 1
        right_index -= 1

msg = list('hello')
print(msg)

msg2 = ['A', 'B', 'C', 'D', 'E']
reverse_inplace(msg2)
print(msg2)