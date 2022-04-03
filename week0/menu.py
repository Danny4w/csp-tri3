# Christmas Tree
#displays the top of the xmas tree
def ttree(n):
    for i in range(n):
        for x in range(n-i):
            print(' ', end=' ')
        for y in range(2*i+1):
            print('o', end=' ')
        print()

#displays the trunk of xmas tree
def btree(n):
    for x in range(3):
        for i in range(n-1):
            print(' ', end=' ')
        print('o o o')

#displays full tree
def christmastree():
    row = int(input('Enter number of rows: '))
    ttree(row)
    ttree(row)
    btree(row)

# Swap
#displays 2 numbers in ascending order
def swap():
    a = int(input("First Number?: "))
    b = int(input("Second Number?: "))
    if a > b:
        print(b,a)
    else:
        print(a,b)

#submenu
def o1():
    print('This is the First Option')
def o2():
    print('This is the Second Option')

def buildMenu(menu):
    for key,value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}")
    print("What is your choice? (enter the number value) ")

def presentMenu(menu):
    buildMenu(menu)
    choice = int(input())
    if (choice) in menu:
        if menu[choice]["type"] == "func":
            menu[choice]["exec"]()
        else:
            presentMenu(menu[choice]["exec"])

#dispays keypad
def print_matrix():
    matrix = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    for x in matrix:
        print(*x)

#defines a sample sub menu
subMenu = {
    1: {"display":"Daniel",
        "exec":o1,
        "type":"func"},
    2: {"display":"Is Cool",
        "type":"func",
        "exec":o2,}
}
#defines the main menu
mainMenu = {
    1: {"display":"Christmas Tree",
        "exec":christmastree,
        "type":"func"},
    2: {"display":"Keypad ",
        "exec":print_matrix,
        "type":"func"},
    3: {"display":"Swap ",
        "exec":swap,
        "type":"func"},
    4: {
        "display":"Submenu",
        "exec": subMenu,
        "type":"submenu"
    }
}

if __name__ == "__main__":
    presentMenu(mainMenu)