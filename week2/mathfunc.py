#Hack 3: Select your own Math function. Write it in Imperative and OOP form. Some Math functions have been provided. Think about inputs and outputs to present to Teacher. It is preferred to have Test data, not input to illustrate code.

# Function to find the minimum between 2 numbers
def findMin(num1, num2):
    if num1 > num2:
      return num2
    else:
      return num1

# Function to find the max between 2 numbers
def findMax(num1, num2):
    if num1 > num2:
      return num1
    else:
      return num2

# Function to find the average between 2 numbers
def findAvg(num1, num2):
    num3 = (num1 + num2) / 2
    return num3

# Function to print elements
def min_max_avg(a, b):
    min_val = findMin(a, b)
    max_val = findMax(a, b)
    avg_val = findAvg(a, b)
    print("min of {0} and {1} is: {2}".format(a, b, min_val))
    print("max of {0} and {1} is: {2}".format(a, b, max_val))
    print("avg of {0} and {1} is: {2}".format(a, b, avg_val))
    print()
    return

def do_mma():
    a = int(input(" Enter the First Value : "))
    b = int(input(" Enter the Second Value : "))
    min_max_avg(a,b)
    return


#test data 
#min_max_avg(8,6)
#min_max_avg(20,30)
#min_max_avg(400,600)