for i in range(1, 72):
  n = i // 9 + 2
  m = i % 9 + 1
  print('%d x %d = %d' % (n, m, n * m))
