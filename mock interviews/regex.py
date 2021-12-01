# MINE:
# def is_match(text, pattern):
#   pass # your code goes here
#   # text="abc" pattern="ab*c"   * = 1

#   # zero, one, more
  
#   s = 0 # text pointer
#   t = 0 # pattern pointer
  
#   while s < len(text):
#     if text[s] == pattern[t] or pattern[t] == '.': # dot wild card

#       s += 1
#       t += 1
      
#     elif pattern[t + 1] == '*':
#         t += 2
      
#     elif pattern[t] == '*':
#       # check
#       # if text[s] != text[s + 1]: # (one case)
#       #    s += 1
#       #    t += 1