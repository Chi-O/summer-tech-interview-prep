import sys

def solution(A):
  """Your solution goes here."""
  # keep track of number of rows
  # create new rows, keep track of running max

  rows = []

  for i in range(len(A)):
    if i == 0:
     rows.append([A[i]])
    else:
      total_max = max(map(max, rows))
      if A[i] > total_max:
        rows.append([A[i]])
      else:
        rows[0].append(A[i])
  
  return len(rows)

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
