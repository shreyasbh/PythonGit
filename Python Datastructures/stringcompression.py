def stringCompression(string):
  count = 1
  compStr = ""
  if len(string) == 0:
    return ""
  if len(string) == 1:
    return string + str(1) 
  for i in range(len(string)-1):
    if string[i] == string[i+1]:
      count += 1
    else:
      compStr = compStr + string[i] + str(count) 
      count = 1
  compStr = compStr + string[i] + str(count) 
  print compStr
  
  
stringCompression("AAAcccDDD")      