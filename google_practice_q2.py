import sys

def solution(A):
  """Your solution goes here."""
  sys.stderr.write('Tip: Use sys.stderr.write() to write debug messages on the output tab.\n')
  pass


def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
