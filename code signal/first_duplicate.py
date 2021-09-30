# naive solution
# def firstDuplicates(a):
  # dub_indices = []
    
  # for i in range(len(a)):
  #   for j in range(i + 1, len(a)):
  #     if a[i] == a[j]:
  #       dub_indices.append(j)
  #       break
  # if len(dub_indices) != 0:
  #   return a[min(dub_indices)]
  # else:
  #   return -1

# a bit optimized
# def firstDuplicates(a):
#   dub_indices = []
#   copy = set()

#   for i in range(len(a)):
#     if a[i] in copy:
#       dub_indices.append(i)
#     else:
#       copy.add(a[i])
  
#   if len(dub_indices) != 0:
#     return a[min(dub_indices)]
#   else:
#     return -1

# more optimized
def first_duplicates(a):
  copy = set()

  for i in range(len(a)):
    if a[i] in copy:
      return a[i]
    else:
      copy.add(a[i])
  
  return -1
  
if __name__ == "__main__":
  a = [2, 1, 3, 5, 3, 2]
  b = [2, 4, 3, 5, 1]
  
  print(first_duplicates(a))