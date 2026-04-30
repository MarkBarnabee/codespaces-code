import pandas as pd
import matplotlib.pyplot as plt

class Point:
    def __init__(self, name, points):
        self.name = name
        self.points = points

def ask():
    jal = input("add another player? (y/n): ")
    print(jal)
    if jal == "y":
        gather()
    else:
        makeInst(listed)
i = 0
def makeInst(listed):
    for i in len(listed):
        Point(str(listed[i][0]), listed[i][1])
        i = i + 1
        print (Point)
    
    
def makePlot(x, y, title, xtitle, ytitle):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.show()

listed = []

def gather():
    global listed
    jay = []
    i = 1
    section = "y"
    name = input("Your name?: ")
    print(name)
    point1 = int(input(f"points for game {i}?: "))
    jay.append(point1)
    print(point1)
    i = 2
    point2 = int(input(f"points for game {i}?: "))
    jay.append(point2)
    print(point2)
    section = input("add another game? (y/n): ")
    while section == "y":
        i = i + 1
        pointi = int(input(f"points for game {i}?: "))
        jay.append(pointi)
        print(jay)
        section = input("add another game? (y/n): ")
    print(name)
    print(jay)
    conf = input("is this correct? (y/n): ")
    print(conf)
    if conf == "y":
        listed.append([name, jay])
        print(listed)
        ask()
    else:
        fun = input("Remake? (y/n): ")
        if fun == "y":
            gather()
        else:
            sursur = input("go with this data? (y/n): ")
            if sursur == "y":
                listed.append([name, jay])
                print(listed)
                ask()
            else:
                print("removed player")
                gather()


#def create_dogs(dog_data):
#    """Function to create multiple instances from a list of variables."""
#    # Using list comprehension for efficiency
#    return [Dog(name, age) for name, age in dog_data]

# Variables to be used for instances
#data = [("Buddy", 3), ("Max", 5), ("Bella", 2)]


gather()