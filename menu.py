from week0.menu import mainMenu
from week1.fibll import fibonacci
from week1.fibll import listl

from week2.factorial import Factorial
from week2.mathfunc import do_mma
from week2.palindrome import do_pal



week0 = {
    1: {
        "display":"week0 menu",
        "exec":mainMenu,
        "type":"submenu"
    },
    0: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}
week1 = {
  1: {
    "display": "Fibonacci",
    "exec": fibonacci,
    "type": "func"
  },
  2: {
    "display": "Lists & Loops",
    "exec": listl,
    "type": "func"
  },
  0: {
    "display": "Quit",
    "exec": quit,
    "type": "func"
  }
}
week2 = {
    1: {
        "display":"Factorial",
        "exec": Factorial,
        "type":"func"
    },
    2: {
        "display":"Math Function: avg, min, max Numbers",
        "exec": do_mma,
        "type":"func"
    },
    3: {
        "display":"EC: Palindrome",
        "exec":do_pal,
        "type":"func"
    },
    0: {
        "display":"Quit",
        "exec":quit,
        "type":"func"
    }
}

mainMenu = {
    1: {
        "display": "Week 0",
        "exec": week0,
        "type": "submenu"
    },
    2: {
        "display": "Week 1",
        "exec": week1,
        "type": "submenu"
    },
    3: {
        "display": "Week 2",
        "exec": week2,
        "type": "submenu"
    },

    0: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}

def buildMenu(menu):
    for key,value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}") # each menu item is printed
    print("What is your choice? (enter the number value) ") # user input promp

def presentMenu(menu):
    buildMenu(menu) #print out menu and take input
    choice = int(input())
    while choice not in menu: # ensure that choice is valid
        choice = int(input("Please elect a valid item. "))
    if (choice) in menu:
        if menu[choice]["type"] == "func": #determine whether recursion is needed
            menu[choice]["exec"]() #run function
        else:
            presentMenu(menu[choice]["exec"]) #display submenu

if __name__ == "__main__":
  while True:
    presentMenu(mainMenu)



