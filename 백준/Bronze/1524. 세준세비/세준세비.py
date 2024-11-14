test_case = int(input())
for _ in range(test_case):
  input()
  sejun, sebin = map(int, input().split())
  
  s_power = sorted(list(map(int, input().split())))
  b_power = sorted(list(map(int, input().split())))

  while len(s_power)!= 0 and len(b_power)!=0:
    if s_power[0] < b_power[0]:
      del s_power[0]
    elif s_power[0] >= b_power[0]:
      del b_power[0]
    
  if len(s_power) == 0:
    print('B')
  elif len(b_power) == 0:
    print('S')
  else:
    print('C')