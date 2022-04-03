from week0.menu import mainMenu
from week1.fibill import fibonacci
from week1.fibill import listl
from week2.factorial import do_fact
from week2.mathfunc import do_mma
from week2.palindrome import do_pal



week0 = {
    0: {
        "display": "Back",
        "exec":quit,
        "type":"back"
    },
    1: {
        "display":"week0 menu",
        "exec":mainMenu,
        "type":"submenu"
    },

}
week1 = {
    0: {
        "display": "Back",
        "exec": quit,
        "type": "back"
    },
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
}
week2 = {
    0: {
        "display":"Back",
        "exec":quit,
        "type":"back"
    },
    1: {
        "display":"Factorial",
        "exec": do_fact,
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
}

MMenu = {
    0: {
        "display": "Week 0",
        "exec": week0,
        "type": "submenu"
    },
    1: {
        "display": "Week 1",
        "exec": week1,
        "type": "submenu"
    },
    2: {
        "display": "Week 2",
        "exec": week2,
        "type": "submenu"
    },

    3: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}

def buildMenu(menu):
    print(" ")
    print("-----------------")
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
            if menu[choice]["type"] != "back":
                presentMenu(menu[choice]["exec"]) #display submenu

if __name__ == "__main__":
    while True:
        presentMenu(MMenu)



