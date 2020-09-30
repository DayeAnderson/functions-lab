# ONE

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum


# TWO
def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest

# THREE
def occurances(string, substr):
  return string.count(substr)

# FOUR
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product
