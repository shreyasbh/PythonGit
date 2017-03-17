def calculateNumberOfPairs(arr,req):
  if len(arr) < 2:
    return 
  
  seen = set()
  output = set()
  
  for num in arr:
    target = req - num 
    if target not in seen:
      seen.add(num)
    else:
      output.add((min(num,target), max(num,target)))
  print("\n".join(map(str,list(output))))
  return len(output)

print(calculateNumberOfPairs([3,2,4,1],5))