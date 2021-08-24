"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

for each character in the string, 
compare to other characters after it
return false if match found 
"""

def is_unique(msg):
  if len(msg) > 128:
    return False

  char_array = [(False) for i in range(0, 128)]

  for i in range(len(msg)):
    char_code = ord(msg[i])

    if (char_array[char_code]):
      return False

    char_array[char_code] = True

  return True

# without data structure
def is_unique2(msg):
  str_length = len(msg)
  for i in range(str_length):
    for j in range(i + 1, str_length):
      if msg[i] == msg[j]:
        return False
  
  return True

if __name__=="__main__":
  print(is_unique2("helo"))