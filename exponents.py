#Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

def exponents(bases, powers):
  list =[]
  for base in bases:
    for power in powers:
      list.append(base ** power)
  return list

print(exponents([2, 3, 4], [1, 2, 3]))