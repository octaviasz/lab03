# Author: Octavia Szkutnik oas5135@psu.edu
# Collaborator: Daniel Chai dac5934@psu.edu
# Collaborator: Abeer Mathur aqm6537@psu.edu
# Collaborator: Sonvi Kharbanda snk5287@psu.edu
# Section 1
# Breakout room 6

def sum_n(num):
  n = int(stuff)
  if(n>1):
    return n + sum_n(n - 1)
  else:
    return 1

def print_n(s, n):
    numtimes = int(n)
    word = str(n)
    if (numtimes> 0):
      print (f"{s}\n")
      print_n(s,numtimes-1)
    else:
      return 0


def run():
  stuff = int(input("Enter an int: "))
  print(f"sum is {sum_n(stuff)}\n")
  stuff2 = str(input("Enter a string: "))
  print_n(stuff2,stuff)

run ()

