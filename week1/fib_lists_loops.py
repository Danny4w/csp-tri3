#Hack 1
InfoDb = []
InfoDb.append({  
               "FirstName": "Daniel",  
               "LastName": "Bertino",  
               "Residence": "San Diego", 
               "DOB": "March 14",
               "Age": "18",
               "Sports": ["Basketball","Soccer"],
               "Fav_Food": "Pizza",
               "School": "DNHS",
               "Subjects": ["cs","stats","literature","econ"]
              })  
x = InfoDb[0]["Sports"][1]
print("sport 1", x)
x = InfoDb[0].get("Sports")[2]
print=("sport 2:", x)

#Hack 2
def For_loop():
    print("For loop")
    for_loop()
  
def While_loop():
    print("While loop")
    while_loop(0)  # requires initial index to start while
    
def Recursive_loop():
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

#Hack 3
def fibonacci():
    num = int(input("15: "))
    # check if the number is negative
    if num < 0:
        print("factorial does not exist for negative numbers")
    else:
        print("The factorial of",num, "is", recur_factorial(num))
