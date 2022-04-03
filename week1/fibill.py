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

#displays part of list
def rec_print(i):
    print(InfoDb[i]["FirstName"], InfoDb[i]["LastName"])
    x = InfoDb[0]["Sports"][0]
    print("sport 1", x)
    x = InfoDb[0].get("Sports")[1]
    print("sport 2:", x)


#Hack 2
#displays all elements of list
def for_loop():
    for i in range(len(InfoDb)):
        rec_print(i)
    return

def while_loop(i):
    i = 0
    while i < len(InfoDb):
        rec_print(i)
        i += 1
    return

def recursive_loop(i):
    if i < len(InfoDb):
        rec_print(i)
        recursive_loop(i+1)
    return

#displays the records using the different loops
def listl():
    print("For loop:")
    for_loop()
    print("---------")

    print("While loop:")
    while_loop(0)
    print("---------")

    print("Recursive loop:")
    recursive_loop(0)
    print("---------")
    return

#definition of recursive fib function
def fib(n):
    #print("Recursive loop")
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)


#Hack 3
#calls recursive fib
def fibonacci():
    num = int(input("enter a number: "))
    # check if the number is negative
    if num < 0:
        print("fibonacci does not exist for negative numbers")
    else:
        print("The fibonacci of", num, "is", fib(num))
