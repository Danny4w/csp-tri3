#class implementation of factorial function
class factorial:

    #initializes class local var
    def __init__(self):
        self.final = [1]

    #main function of factorial
    def __call__(self,n):
        if n < len(self.final):
            return 1
        else:
            f_number = n * self(n-1)
            self.final.append(f_number)
        return self.final[n]

#creates an object of factorial class & displays results
def do_fact():
    obj = factorial()
    n = int(input("n = "))  #user input
    print(obj(n))
    return

if __name__ == "__main__":
    do_fact()
