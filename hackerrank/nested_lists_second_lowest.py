# yes, this works, but it's doing way too much
# time: O(N log N) -> sorts twice
# space: O(N) -> stores scores in another array
# https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
  records = []
  scores = []

  for _ in range(int(input())):
    name = input()
    score = float(input())

    this_record = [name, score]
    records.append(this_record)

    if score not in scores:
      scores.append(score)

    scores.sort()

  for record in sorted(records):
    if record[1] == scores[1]:
      print(str(record[0]))