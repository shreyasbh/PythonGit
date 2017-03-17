def larContinuousSum(arr):
  if len(arr) == 0:
    return 0
  
  maxSum = curSum = arr[0]
  
  for num in arr[1:]:
    curSum = max(curSum+num, num)
    maxSum = max(curSum,maxSum)
  return maxSum 