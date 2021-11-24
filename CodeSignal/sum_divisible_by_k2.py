if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5]
  k = 3

  # freq = [0 for i in range(k)]
  freq = {}
  for i in range(k):
    freq[i] = 0

  ans = 0

  for i in range(len(arr)):
    rem = arr[i] % k

    ans += freq[(k - rem) % k]

    freq[rem] += 1
  
  print(ans)