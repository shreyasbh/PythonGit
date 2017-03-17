def unique(s):
  return len(s) == len(set(s))

print(unique("abccde"))

def unique2(s):
  chars = set()
  for i in s:
    if i in set:
      return False
    else:
      chars.add(i)
      
print(unique("abcde"))

