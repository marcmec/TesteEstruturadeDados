def solution(string):
  s = []
  for i in range(len(string) - 1, -1, -1):
    s.append(string[i])
  return ''.join(s)

print(solution("abcdf"))