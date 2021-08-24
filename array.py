if __name__=="__main__":
  new = {}

  new[0] = []
  new[0].append([1])
  new[0].append([3])

  x = [8]

  if x not in new[0]:
    new[0].append(x)

  print(new.values())

  print([3, 4] == [4, 3])