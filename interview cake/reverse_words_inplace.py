def reverse_inplace(msg, left_index, right_index):
    # while they don't meet (middle char will be left untouched)
    while left_index < right_index:
        # swap characters
        msg[left_index], msg[right_index] = msg[right_index], msg[left_index]

        # move towards the middle
        left_index += 1
        right_index -= 1

def reverse_message(msg):
    reverse_inplace(msg, 0, len(msg) - 1) # inititally reverse entire string

    # keep track of the start index of the current word
    curr_start_index = 0 
    
    # '+ 1" so that we know when we reach the end of the last word
    for i in range(len(msg) + 1):
        # found the end of the current word or end of string
        if i == len(msg) or msg[i] == ' ':
            # 'i - 1' is the char before the space
            # reverse that word
            reverse_inplace(msg, curr_start_index, i - 1)

            """
            I did this at first:
            >> reverse_inplace(msg[curr_start_index:i])
            why doesn't this work? because the slicing actually makes a copy of the list, and does not modify the original list
            when running this, it didn't reverse each word, but only reversed the whole list
            """

            # next word starts after the space (if we're not at the end of the list yet)
            curr_start_index = i + 1

msg = list('cake pound steal')

print(''.join(msg))

reverse_message(msg)

print(''.join(msg))