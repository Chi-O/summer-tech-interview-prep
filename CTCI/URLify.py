def urlify(msg, true_length):
  space_count = 0
  for i in range(true_length):
    if msg[i] == ' ':
      space_count += 1
  
  new_length = true_length - space_count + (space_count * 3)

  msg = list(msg)

  for i in range(true_length - 1, -1, -1):
    if msg[i] == ' ':
      msg[new_length - 1] = '0'
      msg[new_length - 2] = '2'
      msg[new_length - 3] = '%'
      new_length -= 3
    else: 
      msg[new_length - 1] = msg[i]
      new_length -= 1

  
  return " ".join(msg)


if __name__ == '__main__':
  print(urlify("Mr John Smith    ", 13))