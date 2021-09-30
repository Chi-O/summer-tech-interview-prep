arr = [1, 2, 3, 4, 5]
N = len(arr)
S = sum(arr)

dp = [[0 for i in range(S + 1)] for j in range(N + 1)]

for row in dp:
  print(row)
# print(f"initially {dp}")

for i in range(N + 1):
  dp[i][0] = True

print("step 1")
for row in dp:
  print(row)


for j in range(1, S + 1):
  dp[0][j] = False

print("step 2")
for row in dp:
  print(row)
