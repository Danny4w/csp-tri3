#Hack 2: Write Factorial function using classes, providing implementation of call.
  #-Print final number
class Factorial:
    def __init__(self):
      self.fact = 1
    def __call__(self, n):
      for x in range(2, n+1):
        self.fact = self.fact * x;
      
      return self.fact

D_facto = Factorial()    # instantiate the class object and run __init__

#n=int(input("enter a positive number : "))
#print(D_facto(n))            # execute __call__ and print result