def sentenceReversal(inp):
  print(" ".join(inp.strip().split(" ")[::-1]))
  
def sentenceReversal2(inp):
  spaces = [" "]
  words = []
  i = 0
  while i < len(inp):
    if inp[i] not in spaces:
      wordstart = i
      while inp[i] not in spaces:
        i+=1
      words.append(inp[wordstart:i])
    i += 1
  for i in range(len(words)):
    print(words[len(words)-i-1],)
      
sentenceReversal("John is good  ")
sentenceReversal2(" John is good  ")