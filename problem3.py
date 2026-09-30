### add your code here
def is_sorted(list):
  """
  ### add to the docstring including additional doctests
  some list -> True list in ascending order and  descending order, false otherwise
  takes in a list of numbers and returns True if they are in increasing or decreasing order and False otherwise.
  >>> is_sorted([1,3,5.6,7])
  True
  >>> is_sorted([1, 3, 5.6, 7])
  True
  >>> is_sorted([7, 5.6, 3, 1])
  True
  >>> is_sorted([1])
  False
  >>> is_sorted([2,4,6,8,10])
  True
  >>> is_sorted([10,9,8,7])
  True
  >>> is_sorted([9,28,0,5])
  False
  """
  increasing = True
  decreasing = True

  if len(list) < 2:
    return False

  for i in range(len(list)):
    if i + 1 < len(list):

      if list[i] > list[i + 1]:
        increasing = False

      if list[i] < list[i + 1]:
        decreasing = False

  if increasing or decreasing:
    return True
  else:
    return False



