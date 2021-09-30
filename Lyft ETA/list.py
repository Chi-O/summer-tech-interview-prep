list =  [1, 3, 4, 5, 6, 7]

for index in range(len(list) - 1, 0, -1):
  temp = list[index]
  list[index] = list[index - 1]
  list.append(temp)

print(list)
  
