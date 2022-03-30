#Hack 4: Extra Credit. Write Palindrome function using classes, providing implementation of call.

import re

class Palindrome:
    # init method
    def __init__(self, sentence):

      #initialize variables
      self.string = sentence     # make a copy
      self.palindrome_ok = False # assume is false
      self.tests = []            # array of tests
      self.count = 0             # counter for tests

      # extract alphanumeric characters and convert to lowercase 
      self.alpnum = re.sub(r'[^a-zA-Z0-9]', '', self.string).lower()  
      self.length = len(self.alpnum)    

      # perform checking
      self.__call__()  

    # palindrome tester method
    def __call__(self):

      # extreme case: short string
      if self.length <= 1: 
        self.palindrome_ok = True
        return
          
      # split string in two parts / in the middle
      mid = int(self.length / 2)
      part1 = self.alpnum[0:mid]
      if (self.length % 2 == 0) : 
        part2 = self.alpnum[mid:self.length]
      else:
        part2 = self.alpnum[mid+1:self.length]

      part2r = ''.join(reversed(part2))

      if (part1 == part2r) :
        self.logger(part1, part2, True)
        self.palindrome_ok = True
      else:
        self.logger(part1, part2, False)

      return
      
    # palindrome logging
    def logger(self, part1, part2, result):
      self.tests.append({"test": self.string, "part1": part1, "part2": part2, "result": result})

      
# Tester Code
def pal():      
  good = "Race car"
  bad = "onomatopoeia"
  goodphrase = "A man, a plan, a canal -- Panama!"
  goodphrase2 = "Evil olive."
  badphrase = "This is not a palindrome!"
  
  Entry1 = Palindrome(good)
  Entry2 = Palindrome(bad)
  Entry3 = Palindrome(goodphrase)
  Entry4 = Palindrome(goodphrase2)
  Entry5 = Palindrome(badphrase)
  
  # access the class attributes
  print(f"{good} is {Entry1.palindrome_ok}")
  print(f"{bad} is {Entry2.palindrome_ok}")
  print(f"{goodphrase} is {Entry3.palindrome_ok}")
  print(f"{goodphrase2} is {Entry4.palindrome_ok}")
  print(f"{badphrase} is {Entry5.palindrome_ok}")

if __name__ == "__main__":
    pal()
#-Evaluate if it is a palindrome
#-Evaluate complex algorithms eliminating spaces, case and special characters. "A man, a plan, a canal -- Panama!"
  #-Use Test data, not input
  #-Illustrate failure