import pandas as pd
import matplotlib.pyplot as plt

class Point:
    _instances = []
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self._instances.append(self)
        

def funcItUp(y, point):
    y does stuff to point


def ask():
    jal = input("add another player? (y/n): ")
    print(jal)
    if jal == "y":
        gather()
    else:
        listed.append(['x', jay2])
        makeInst(listed)
i = 0
def makeInst(listed):
    for i in range(len(listed)):
        Point(str(listed[i][0]), listed[i][1])
        i = i + 1
    for obj in Point._instances:
        print (obj.name)
        print (obj.points)
    makeData(Point._instances)
    
def makeData(data):
    keys = []
    values = []
    for obj in data:
        keys.append(obj.name)
        values.append(obj.points)
    result = dict(zip(keys, values))
    print(result)
    frameData(result)
cool = []
def frameData(res):
    dat = pd.DataFrame(res)
    print(dat)
    global cool
    for col in dat:
        print(col)
        if col != 'x':
            cool.append(str(col))
    makePlot(dat, 'x', cool)

def makePlot(pllt, xl, yl):
    pllt.plot(x = f'{xl}', y = yl)
    plt.title('points per game')
    plt.xlabel('game')
    plt.ylabel('points')
    plt.savefig('my_plot.png') 
    plt.show()
    fr = input("show calculations?(y/n): ")
    if fr == 'y':
        funcItUp(listed)
    else:
        print("See file for graph.")
listed = []
jay2 = []

def gather():
    global listed
    global jay2
    jay = []
    jay2 = []
    i = 1
    section = "y"
    name = input("Your name?: ")
    print(name)
    point1 = int(input(f"points for game {i}?: "))
    jay.append(point1)
    jay2.append(i)
    print(point1)
    i = 2
    point2 = int(input(f"points for game {i}?: "))
    jay.append(point2)
    jay2.append(i)
    print(point2)
    section = input("add another game? (y/n): ")
    while section == "y":
        i = i + 1
        pointi = int(input(f"points for game {i}?: "))
        jay.append(pointi)
        jay2.append(i)
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


if __name__ == '__main__':
    gather()
    