while True:
  n = int(input())
  if n == 0:
    break
  d = {}
  r = 0
  for i in range(n):
    a, b = input().strip().split()
    if (b, a) in d and d[b, a] > 0:
      r += 2
      d[b, a] -= 1
      continue
    d.setdefault((a, b), 0)
    d[a, b] += 1
  if r == n:
    print('YES')
  else:
    print('NO')
