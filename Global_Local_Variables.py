v = 65 #Global Var
def Show():
    global x
    #print(c)  name 'c' is not defined c is not global var
    print("Show Func")
    print(v)
def main():
    global x
    c = 34 #Local Var
    print("c = {}".format(c))
    Show()
    print(v)


if __name__ == '__main__':main()
