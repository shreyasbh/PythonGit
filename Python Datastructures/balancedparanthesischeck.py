def balanceCheck(string):
  if len(string)%2 != 0:
    return False
  opening = set("{([")
  matches = set([("(",")"),("{","}"),("[","]")])
  stack = []
  
  for i in string:
    if i in opening:
      stack.append(i)
    else:
      if len(stack) == 0:
        return False
      lastOpen = stack.pop()
      if (lastOpen, i) not in matches:
        return False 
  return len(stack) == 0

print(balanceCheck('({[]}]'))