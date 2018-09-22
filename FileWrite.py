def main():
    #Write to file
    #output = open("myfile.txt","w")
    output = open("myfile.txt","a")

    #output.write(" hello insha Allah I will be rich,my name is youssef")
    for i in range(5):
        inputTofile = input("enter string to append to file")
        output.write("\n{}".format(inputTofile))
    output.close()
    print("App is Done")
if __name__ == '__main__':main()
